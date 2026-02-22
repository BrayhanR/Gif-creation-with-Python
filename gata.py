import imageio.v3 as iio

filenames = ['gata1.jpeg', 'gata2.jpeg', 'gata3.jpeg']
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('gata.gif', images, duration = 700, loop = 0)