import os
import random
import numpy as np
import open3d as o3d
from tkinter import *
from tkinter.tix import *
from PIL import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from ttkwidgets import CheckboxTreeview
from WFS.Camera import cameraApp
# from CreateMesh import createMesh


root = Tk()
root.title('WPS')
root.geometry('{}x{}'.format(460, 350))

# Functions for widgets

# Image Button -- To load image file
def loadImage():
    path = filedialog.askopenfilename(initialdir="C:/Users/Sandeep Saurav/Desktop/", title="Select a file", filetype=(("PNG","*.png"),("All Files","*.*")))
    apploadImage = Zoom_Advanced(displayFrame, path=path)
    # # label1= Label(treeFrame, text=filename1).pack()
    # imageOpen1 = Image.open(filename1)
    # imageOpenNew = imageOpen1.resize((800,662), Image.ANTIALIAS)
    # imageOpen1 = ImageTk.PhotoImage(imageOpenNew)
    # imageLabel1 = Label(displayFrame, image=imageOpen1)
    # imageLabel1.pack(fill=None, expand=False)     

# Gallary Button -- To load multiple image file
def loadMultipleImage():
    global cnv
    images = []
    path = filedialog.askdirectory()
    for dirname,dirnames, filenames in os.walk(path):
        for filename in filenames:
            file = os.path.join(dirname, filename)
            if '.jpg' in file.lower() or '.gif' in file.lower() or '.png' in file.lower():
                images.append(file)
    cnv = Canvas(displayFrame,width=800, height=640)
    cnv.grid(row=0, column=0, sticky='nswe')
    ## Scrollbars for canvas
    hScroll = Scrollbar(displayFrame, orient=HORIZONTAL, command=cnv.xview)
    hScroll.grid(row=1, column=0, sticky='we')
    vScroll = Scrollbar(displayFrame, orient=VERTICAL, command=cnv.yview)
    vScroll.grid(row=0, column=1, sticky='ns')
    cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
    frm = Frame(cnv)
    cnv.create_window(0, 0, window=frm, anchor='nw')

    # Frame contents
    image_count=0
    columns =5
    for image in images:
        image_count += 1
        r, c = divmod(image_count - 1, columns)
        im = Image.open(image)
        resized = im.resize((150,212), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar = Label(frm, image = tkimage)
        myvar.image = tkimage
        myvar.grid(row=r, column = c, padx=2, pady=2)
    # Update display to get correct dimensions
    frm.update_idletasks()
    # Configure size of canvas's scrollable zone
    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))



# Folder Button -- To load all the contents of the folder or directory
def loadDirectory():
    global directory
    directory = filedialog.askdirectory()
    apploadDirectory = treeViewContent(treeFrame, path=directory)

# Save Button -- To save file
def saveImage():
    #filename3 = filedialog.asksaveasfilename(confirmoverwrite=False, title="Save file", filetype=(("PNG","*.png"),("All Files","*.*")))
    data = [("PNG","*.png"),("JPEG","*.jpeg"),('All tyes(*.*)', '*.*')]
    file = filedialog.asksaveasfilename(confirmoverwrite=False, filetypes = data, defaultextension = data)

# Refresh Button -- to Refresh file
def refresh():
    directory = ''
    
    
    

# Camera Buttuon -- to load camera frame to capture pictures
def loadCamera():
    top = Toplevel()
    cameraApp(top,"Camera")

def createMesh():
    dataname = filedialog.askopenfilename(initialdir="C:/Users/Sandeep Saurav/Desktop/", title="Select a file", filetype=(("3D Object","*.ply"),("All Files","*.*")))
    response = messagebox.askyesno("Generate Mesh", "Do you want to continue?")
    if int(response) == 1 :
        pcd = o3d.io.read_point_cloud(dataname)
        mesh = pcd.get_knot_mesh()
        o3d.visualization.draw_geometries([mesh])
    else: return

def loadPointCloud():
    global pointCloud
    filename1 = filedialog.askopenfilename(initialdir="C:/Users/Sandeep Saurav/Desktop/", title="Select a file", filetype=(("3D Object","*.ply"),("All Files","*.*")))
    cloud = o3d.io.read_point_cloud(filename1) # Read the point cloud
    pointCloud = o3d.visualization.draw_geometries([cloud])   
    pointCloudNew = pointCloud.getresize((800,662), Image.ANTIALIAS)
    pointCloudLabel = Label(displayFrame, image=pointCloudNew)
    pointCloudLabel.pack(fill=None, expand=False)

def openPotree():
    pass

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


# Menu List
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=loadImage)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
# filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)


# frames as Placeholders

widgetFrame = Frame(root, bd=1, relief="sunken", width=450, height=30)
treeFrame = Frame(root, background="#FFFFFF", bd=1, relief="sunken", width=300, height=300)
activityFrame = Frame(root, background="#D2E2FB", bd=1, relief="sunken", width=300, height=362)
displayFrame = Frame(root, background="#FFFFFF", bd=1, relief="sunken", width=800, height=662)
extraFrame = Frame(root, background= "#FFFFFF", bd=1, relief="sunken", width=280, height=662)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


widgetFrame.grid(row=0, column=0, sticky="ew", columnspan=3)
treeFrame.grid(row=1, column=0, sticky="nw")
activityFrame.grid(row=2, column=0, sticky="sw")
displayFrame.grid(row=1, column=1, rowspan=2, sticky="nsew")
extraFrame.grid(row=1, column=2, rowspan=2, sticky="e")


# images for widgets

singleImg = ImageTk.PhotoImage(Image.open("image1/image.png"))
multiImg = ImageTk.PhotoImage(Image.open("image1/image-gallery.png"))
folderImg = ImageTk.PhotoImage(Image.open("image1/folder.png"))
reloadImg = ImageTk.PhotoImage(Image.open("image1/reload.png"))
saveImg = ImageTk.PhotoImage(Image.open("image1/save.png"))
zoominImg = ImageTk.PhotoImage(Image.open("image1/zoom-in.png"))
zoomoutImg = ImageTk.PhotoImage(Image.open("image1/zoom-out.png"))
scrollImg = ImageTk.PhotoImage(Image.open("image1/scroll.png"))
cameraImg = ImageTk.PhotoImage(Image.open("image1/camera.png"))
droneImg = ImageTk.PhotoImage(Image.open("image1/drone.png"))
meshImg = ImageTk.PhotoImage(Image.open("image1/cube.png"))
pointImg = ImageTk.PhotoImage(Image.open("image1/point.png"))
viewImg = ImageTk.PhotoImage(Image.open("image1/visual.png"))

# widgets in widegtframe

singleImg_btn = Button(widgetFrame, image=singleImg, command=loadImage)
singleImg_btn.pack(side='left')
multiImg_btn = Button(widgetFrame, image=multiImg, command=loadMultipleImage)
multiImg_btn.pack(side='left')
folderImg_btn = Button(widgetFrame, image=folderImg, command=loadDirectory)
folderImg_btn.pack(side='left')
reloadImg_btn = Button(widgetFrame, image=reloadImg, command=refresh)
reloadImg_btn.pack(side='left')
saveImg_btn = Button(widgetFrame, image=saveImg, command=saveImage)
saveImg_btn.pack(side='left')
# zoominImg_btn = Button(widgetFrame, image=zoominImg, command=saveImage)
# zoominImg_btn.pack(side='left')
# zoomoutImg_btn = Button(widgetFrame, image=zoomoutImg, command=saveImage)
# zoomoutImg_btn.pack(side='left')
# scrollImg_btn = Button(widgetFrame, image=scrollImg, command=saveImage)
# scrollImg_btn.pack(side='left')
cameraImg_btn = Button(widgetFrame, image=cameraImg, command=loadCamera)
cameraImg_btn.pack(side='left')
droneImg_btn = Button(widgetFrame, image=droneImg)
droneImg_btn.pack(side='left')
meshImg_btn = Button(widgetFrame, image=meshImg, command=createMesh)
meshImg_btn.pack(side='left')
pointImg_btn = Button(widgetFrame, image=pointImg, command=loadPointCloud)
pointImg_btn.pack(side='left')
viewImg_btn = Button(widgetFrame, image=viewImg, command=openPotree)
viewImg_btn.pack(side='left')

## Creating Tool Tip for 

tip = Balloon(root)
#tip.config(bg="white", ) # change boundary color
#tip.label.config(bg="white", fg="green") #  change arrow color
tip.message.config(bg="white",fg="black") # change messgae color
for sub in tip.subwidgets_all():
    sub.configure(bg="white") # to make yellow bg = white
tip.subwidget('label').forget() # to remove arrow

# Binding Tool Tip to Buttons
tip.bind_widget(singleImg_btn, balloonmsg="Open Image")
tip.bind_widget(multiImg_btn , balloonmsg="Open Multiple Image")
tip.bind_widget(folderImg_btn, balloonmsg="Open Folder")
tip.bind_widget(reloadImg_btn, balloonmsg="Refresh")
tip.bind_widget(saveImg_btn, balloonmsg="Save As")
tip.bind_widget(cameraImg_btn, balloonmsg="Open Camera")
tip.bind_widget(droneImg_btn, balloonmsg="Open Drone Imagery")
tip.bind_widget(meshImg_btn, balloonmsg="Create Mesh")
tip.bind_widget(pointImg_btn, balloonmsg="Create Point Cloud")
tip.bind_widget(viewImg_btn, balloonmsg="Open Potree Visualization")

# Contents for treeFrame
class treeViewContent(object):
    def __init__(self, master, path):
        self.nodes = dict()
        self.tree = CheckboxTreeview(treeFrame)
        ysb = Scrollbar(treeFrame, orient='vertical', command=self.tree.yview)
        xsb = Scrollbar(treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading("#0", text='Directory', anchor='w')
        ysb.pack(side=RIGHT, fill=Y )
        xsb.pack(side=BOTTOM, fill=X, anchor='sw')
        self.tree.pack(side=LEFT, anchor="center")
        
        # ysb.grid(row=0, column=1, sticky='ns')
        # xsb.grid(row=1, column=0, sticky='ew')

        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)

    def insert_node(self, parent, text, abspath):

        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))

#----------- Adding Autoscroll and Zoom features to the canvas -------------#
class AutoScrollbar(ttk.Scrollbar):
    ''' A scrollbar that hides itself if it's not needed.
        Works only if you use the grid geometry manager '''
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise TclError('Cannot use pack with this widget')

    def place(self, **kw):
        raise TclError('Cannot use place with this widget')

class Zoom_Advanced(ttk.Frame):
    ''' Advanced zoom of the image '''
    def __init__(self, mainframe, path):
        ''' Initialize the main Frame '''
        ttk.Frame.__init__(self, master=mainframe)
        #self.master.title('Zoom with mouse wheel')
        # Vertical and horizontal scrollbars for canvas
        vbar = AutoScrollbar(self.master, orient='vertical')
        hbar = AutoScrollbar(self.master, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
        # Create canvas and put image on it
        self.canvas = Canvas(self.master, highlightthickness=0,
                                xscrollcommand=hbar.set, yscrollcommand=vbar.set, width=800, height=662, bg="#FFFFFF")
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created
        vbar.configure(command=self.scroll_y)  # bind scrollbars to the canvas
        hbar.configure(command=self.scroll_x)
        # Make the canvas expandable
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        # Bind events to the Canvas
        self.canvas.bind('<Configure>', self.show_image)  # canvas is resized
        self.canvas.bind('<ButtonPress-1>', self.move_from)
        self.canvas.bind('<B1-Motion>',     self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux
        self.canvas.bind('<Button-5>',   self.wheel)  # only with Linux, wheel scroll down
        self.canvas.bind('<Button-4>',   self.wheel)  # only with Linux, wheel scroll up
        self.image = Image.open(path)  # open image
        self.width, self.height = self.image.size
        self.imscale = 1.0  # scale for the canvaas image
        self.delta = 1.3  # zoom magnitude
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
        # Plot some optional random rectangles for the test purposes
        minsize, maxsize, number = 5, 20, 10
        for n in range(number):
            x0 = random.randint(0, self.width - maxsize)
            y0 = random.randint(0, self.height - maxsize)
            x1 = x0 + random.randint(minsize, maxsize)
            y1 = y0 + random.randint(minsize, maxsize)
            #color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
            #self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, activefill='black')
        self.show_image()

    def scroll_y(self, *args, **kwargs):
        ''' Scroll canvas vertically and redraw the image '''
        self.canvas.yview(*args, **kwargs)  # scroll vertically
        self.show_image()  # redraw the image

    def scroll_x(self, *args, **kwargs):
        ''' Scroll canvas horizontally and redraw the image '''
        self.canvas.xview(*args, **kwargs)  # scroll horizontally
        self.show_image()  # redraw the image

    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''
        self.canvas.scan_mark(event.x, event.y)

    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.show_image()  # redraw the image

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        bbox = self.canvas.bbox(self.container)  # get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: pass  # Ok! Inside the image
        else: return  # zoom only inside image area
        scale = 1.0
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down
            i = min(self.width, self.height)
            if int(i * self.imscale) < 30: return  # image is less than 30 pixels
            self.imscale /= self.delta
            scale        /= self.delta
        if event.num == 4 or event.delta == 120:  # scroll up
            i = min(self.canvas.winfo_width(), self.canvas.winfo_height())
            if i < self.imscale: return  # 1 pixel is bigger than the visible area
            self.imscale *= self.delta
            scale        *= self.delta
        self.canvas.scale('all', x, y, scale, scale)  # rescale all canvas objects
        self.show_image()

    def show_image(self, event=None):
        ''' Show image on the Canvas '''
        bbox1 = self.canvas.bbox(self.container)  # get image area
        # Remove 1 pixel shift at the sides of the bbox1
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image in the visible area
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image in the visible area
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        self.canvas.configure(scrollregion=bbox)  # set scroll region
        x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            x = min(int(x2 / self.imscale), self.width)   # sometimes it is larger on 1 pixel...
            y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
            image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)  # set image into background
            self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection



root.config(menu=menubar)

root.mainloop()
