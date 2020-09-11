# kNN image upscaling for low resolution photos
This script was originally written to upscale sets of _small_ images of maps sent by [CanSat](https://en.wikipedia.org/wiki/CanSat) satellite. Because of low bandwidth images had resolution of 16x8 pixels. Thanks to optimization script runs comfortably on images that size do not exceed 640x480 pixels, however it is able to handle bigger ones as well (with more time obviously).
## To do
- [x] Fix to support image files
- [ ] Fix edge condition (Lost after conversion)
- [ ] Bring back multi-type support
- [ ] Add multicolour support
- [ ] Rewrite in c++ to speed process?
