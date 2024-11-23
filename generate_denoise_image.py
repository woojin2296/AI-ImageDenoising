import os.path

import numpy as np

import torch

from utils import utils_image as util

def generate_denoise_image(path, noise_level_img=50):
    noise_level_model = noise_level_img  # noise level for model
    model_name = 'ffdnet_color'          # 'ffdnet_gray' | 'ffdnet_color' | 'ffdnet_color_clip' | 'ffdnet_gray_clip'
    need_degradation = True              # default: True
    show_img = False                     # default: False

    if 'color' in model_name:
        n_channels = 3        # setting for color image
        nc = 96               # setting for color image
        nb = 12               # setting for color image
    else:
        n_channels = 1        # setting for grayscale image
        nc = 64               # setting for grayscale image
        nb = 15               # setting for grayscale image
    if 'clip' in model_name:
        use_clip = True       # clip the intensities into range of [0, 1]
    else:
        use_clip = False
    model_pool = 'models'  # fixed
    model_path = os.path.join(model_pool, model_name+'.pth')

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    from models.network_ffdnet import FFDNet as net
    model = net(in_nc=n_channels, out_nc=n_channels, nc=nc, nb=nb, act_mode='R')
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    for k, v in model.named_parameters():
        v.requires_grad = False
    model = model.to(device)

    img_name, ext = os.path.splitext(os.path.basename(path))
    img_L = util.imread_uint(path, n_channels=n_channels)
    img_L = util.uint2single(img_L)
    if need_degradation:  # degradation process
        np.random.seed(seed=0)  # for reproducibility
        img_L += np.random.normal(0, noise_level_img/255., img_L.shape)
        if use_clip:
            img_L = util.uint2single(util.single2uint(img_L))
    util.imshow(util.single2uint(img_L), title='Noisy image with noise level {}'.format(noise_level_img)) if show_img else None
    img_L = util.single2tensor4(img_L)
    img_L = img_L.to(device)
    sigma = torch.full((1,1,1,1), noise_level_model/255.).type_as(img_L)
    img_E = model(img_L, sigma)
    img_E = util.tensor2uint(img_E)
    # util.imsave(img_E, os.path.join(os.path.dirname(path), img_name+'_ffdnet'+ext))

    return img_E


# def main():
#     # image_path = os.path.join(os.path.expanduser('~'), 'Downloads', '620c02da6b65b59cdd65d987_Bill Maynard - Mink zoom.jpg')
#     image_path = '/Users/ubicomp/Downloads/620c02da6b65b59cdd65d987_Bill Maynard - Mink zoom.jpg'
#     image = generate_denoise_image(image_path, noise_level_img=100)
#     util.imshow(image)
#     img_name, ext = os.path.splitext(os.path.basename(image_path))
#     util.imsave(image, os.path.join(os.path.dirname(image_path), img_name+'_ffdnet'+ext))

# if __name__ == '__main__':
#     main()