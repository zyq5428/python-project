import shelve

shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Poola', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()