import matplotlib.pyplot as plt

def graph_generator(fii_data):

 
    # Step 1. Create a scatter chart
    x = fii_data.pop('ROE')
    y = fii_data.pop('P_L')
    names = fii_data.pop('ASSET_NAME')


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    scatter = ax.scatter(
        x,
        y
    )

    # Step 2. Create Annotation Object
    annotation = ax.annotate(
        text='',
        xy=(0, 0),
        xytext=(15, 15), # distance from x, y
        textcoords='offset points',
        bbox={'boxstyle': 'round', 'fc': 'w'},
        arrowprops={'arrowstyle': '->'}
    )
    annotation.set_visible(False)


    # Step 3. Implement the hover event to display annotations
    def motion_hover(event):
        annotation_visbility = annotation.get_visible()
        
        if event.inaxes == ax:
            
            is_contained, annotation_index = scatter.contains(event)    
            
            if is_contained:
                
                data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                annotation.xy = data_point_location
            
                text_label = (names[annotation_index['ind'][0]],'({0:.2f}, {1:.2f})'.format(x[annotation_index['ind'][0]],y[annotation_index['ind'][0]]))
                annotation.set_text(text_label)

                annotation.get_bbox_patch().set_facecolor('w')
                annotation.set_alpha(0.4)

                annotation.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if annotation_visbility:
                    annotation.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect('motion_notify_event', motion_hover)
    ax.set_title('Ações ROE/P_E')
    ax.set_xlim(0,70)
    ax.set_ylim(0,70)
    ax.set_xlabel('ROE (Return over equity)')
    ax.set_ylabel('P/E (Price earning)')
    plt.show()
     
     