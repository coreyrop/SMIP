"""
Destroys all content inside of the given frame
frame: frame who's content will be destroyed
"""
def destroy_content(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    pass


"""
Destroys the given frames content and then draws new content to that frame using the given function
current_frame: frame who's content will be changed
draw_function: function that will be called to draw new content
"""
def transfer_to(current_frame, draw_function):
    destroy_content(current_frame)
    draw_function()
    pass