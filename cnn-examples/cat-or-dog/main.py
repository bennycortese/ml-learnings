def forward_propagation_for_predict(image, model):
    image = image / 255
    result = model.predict(image)
    return result

def augment_data(images, labels):
    pass
