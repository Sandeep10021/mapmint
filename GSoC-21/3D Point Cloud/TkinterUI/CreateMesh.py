import numpy as np
import open3d as o3d
from tkinter import filedialog
from tkinter import messagebox

def createMesh():
    #create paths and load data
    dataname = filedialog.askopenfilename(initialdir="C:/Users/Sandeep Saurav/Desktop/", title="Select a file", filetype=(("3D Object","*.ply"),("All Files","*.*")))
    point_cloud= np.loadtxt(pcd,skiprows=1)

    response = messagebox.askyesno("Generate Mesh", "Do you want to continue?")
    if int(response) == 1 :
        #Format to open3d usable objects
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
        pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
        o3d.geometry.estimate_normals(
        pcd,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
                                                          max_nn=30))
        pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])

        """# Choose a meshing strategy

        Now we are ready to start the surface reconstruction process by meshing the pcd point cloud.

        # Process the data

        ## Strategy 1: BPA
        """
        #radius determination
        distances = pcd.compute_nearest_neighbor_distance()
        avg_dist = np.mean(distances)
        radius = 3 * avg_dist

        #computing the mehs
        bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))

        #decimating the mesh
        dec_mesh = o3d.mesh.simplify_quadric_decimation(100000)

        """*Optional ---*"""

        dec_mesh.remove_degenerate_triangles()
        dec_mesh.remove_duplicated_triangles()
        dec_mesh.remove_duplicated_vertices()
        dec_mesh.remove_non_manifold_edges()

        """## Strategy 2: Poisson' reconstruction"""

        #computing the mesh
        poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]

        #cropping
        bbox = pcd.get_axis_aligned_bounding_box()
        p_mesh_crop = poisson_mesh.crop(bbox)

        """# Export and visualize"""

        #export
        output_path = filedialog.askdirectory()
        o3d.io.write_triangle_mesh(output_path+"bpa_mesh.ply", dec_mesh)
        o3d.io.write_triangle_mesh(output_path+"p_mesh_c.ply", p_mesh_crop)

        #function creation
        def lod_mesh_export(mesh, lods, extension, path):
            mesh_lods={}
            for i in lods:
                mesh_lod = mesh.simplify_quadric_decimation(i)
                o3d.io.write_triangle_mesh(path+"lod_"+str(i)+extension, mesh_lod)
                mesh_lods[i]=mesh_lod
            print("generation of "+str(i)+" LoD successful")
            return mesh_lods

        #execution of function
        my_lods = lod_mesh_export(bpa_mesh, [100000,50000,10000,1000,100], ".ply", output_path)

        #execution of function
        my_lods2 = lod_mesh_export(bpa_mesh, [8000,800,300], ".ply", output_path)
    
    else:
        dataname.delete(0,"end")

createMesh()
