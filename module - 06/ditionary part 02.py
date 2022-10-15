mobile = {'name': 'Samsung a52',
          'brand': 'Samsung',
          'country': 'Bangladesh',
          'camera':'48mp',
          'ram': '8 GB',
          'rom': '128'
          }
print(mobile['ram'])
print(mobile.get('rom'))

print(mobile)
mobile['rom'] = '32GB'
print('Rom update: 32 GB')
mobile.update({'camera': '10mp'})
print(mobile)
