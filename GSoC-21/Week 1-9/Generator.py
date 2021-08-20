import uno
import getopt, sys

from unohelper import Base, systemPathToFileUrl, absolutize

from com.sun.star.beans import PropertyValue
from com.sun.star.script import CannotConvertException
from com.sun.star.lang import IllegalArgumentException
from com.sun.star.task import ErrorCodeIOException
from com.sun.star.io import IOException, XOutputStream

class OutputStream( Base, XOutputStream ):
    def __init__( self ):
        self.closed = 0
    def closeOutput(self):
        self.closed = 1
    def writeBytes( self, seq ):
        sys.stdout.write( seq.value )
    def flush( self ):
        pass

def PointCloud(conf,inputs,outputs):
	# get the uno component context from the PyUNO runtime  
	localContext = uno.getComponentContext()

	# create the UnoUrlResolver 
	# on a single line
	resolver = 	localContext.ServiceManager.createInstanceWithContext	("com.sun.star.bridge.UnoUrlResolver", localContext )

	# connect to the running office                                 
	ctx = resolver.resolve( conf["oo"]["server"].replace("::","=")+";urp;StarOffice.ComponentContext" )
	smgr = ctx.ServiceManager

	# get the central desktop object
	desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)

	# get the file name
	adressDoc=systemPathToFileUrl(conf["main"]["dataPath"]+"/"+inputs["InputDoc"]["value"])

	propFich=PropertyValue("Hidden", 0, True, 0),

	myDocument=0
	try:
	    myDocument = desktop.loadComponentFromURL(adressDoc,"_blank",0,propFich)
	except CannotConvertException, e:
	    print >> sys.stderr,  'Cannot Generate the Point Cloud : \n'
	    print >> sys.stderr,  e
	    sys.exit(0)
	except IllegalArgumentException, e:
	    print >> sys.stderr,  'Cannot Generate the Point Cloud : \n'
	    print >> sys.stderr,  e
	    sys.exit(0)

	outputDoc=systemPathToFileUrl(conf["main"]["tmpPath"]+"/"+inputs["OutputDoc"]["value"])

	tmp=inputs["OutputDoc"]["value"].split('.');

	outputFormat={"ply": "writer_ply_export", "html": "HTML (StarWriter)","odt": "writer8","doc": "MS Word 97","rtf": "Rich Text Format"}

	for i in range(len(outputFormat)) :
	    if tmp[1]==outputFormat.keys()[i] :
	        filterName=outputFormat[tmp[1]]
	        prop1Fich = (
	            PropertyValue( "FilterName" , 0, filterName , 0 ),
		        PropertyValue( "Overwrite" , 0, True , 0 )
	        )
	        break

	myDocument.storeToURL(outputDoc,prop1Fich)
	myDocument.close(True)
	ctx.ServiceManager
	outputs["OutputedDocument"]={"value": inputs["OutputDoc"]["value"],"dataType": "string"}
	return 3
