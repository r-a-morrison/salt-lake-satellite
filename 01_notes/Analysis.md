# Analysis

TorchGeo includes a variety of pre-trained models that have been trained with multi-spectral satellite imagery.

Information about TorchGeo models can be found [here](https://torchgeo.readthedocs.io/en/stable/api/models.html). There is only one paper that has pre-trained on LandSat 8 & 9 OLI and TIRS data with 11 spectral bands ([Stewart et al., 2023](https://arxiv.org/pdf/2306.09424.pdf)).

For Landsat 8 & 9 Spectral Reflectance (SR) data, the `ResNet18_Weights.LANDSAT_OLI_TIRS_TOA_MOCO` model seems to be the highest performing. It struggles for fine details like crop classification, but it seems to perform well on cloud classification, which is somewhat similar to our problem of water classification. There are 5 other Landsat 8 & 9 models available that could further explore.