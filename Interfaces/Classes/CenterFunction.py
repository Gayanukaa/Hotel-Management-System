def center(root,width,height):
    window_width = width
    window_height = height

    scren_width = root.winfo_screenwidth()
    scren_height = root.winfo_screenheight()
    cnter_x = int(scren_width/2 - window_width/2)
    cnter_y = int(scren_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{cnter_x}+{cnter_y}')  