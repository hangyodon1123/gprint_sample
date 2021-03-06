#python gprintm0()
#  for HP Prime non cas

#  title        : gprint1m.py  for Casio fx-CG50, Numworks
#               : gprint2m.py  for TI-84 Plus CE Python
#               : gprint3m.py  for HP Prime non cas
#  version      : 2022-01-24 ver 00.04
#  original     : akatuki (for Casio fx-CG50)
#  modification : hangyodon1123 (for Numworks,TI-84 Plus CE,HP Prime)

#  only import for TI-84 Plus CE Python
#from ti_draw import *

#  only import for HP Prime non cas
from graphic import *

#  functions definitions

#  getting platform id
def getplatform():
  pid = -1  #  non support
  try:
    from casioplot import *
    pid = 0  #  Casio fx-CG50
  except:
    pass
  try:
    from kandinsky import *
    pid = 1  #  Numworks
  except:
    pass
  try:
    import sys
    if sys.platform == 'TI-Python':
      pid = 2  #  TI-84 Plus CE Python
    if sys.platform == 'HP Prime':
      pid = 3  #  HP Prime non cas
  except:
    pass
  return pid

#  plot control
def gprint(pf, colour, x, y, d, st):
  for c in st:
    num = '0123456789ABCDEF'.index(c)
    code = colour[num]
    if pf == 0:    #  for Casio fx-CG50
      for j in range(d):
        for i in range(d):
          set_pixel(x+i, y+j, code)
    elif pf == 1:  #  for Numworks
      fill_rect(x, y, d, d, code)
    elif pf == 3:  #  for HP Prime non cas
      fill_rect(x, y, d, d, code)
    else:          #  for TI-84 Plus CE Python
      set_color(code[0],code[1],code[2])
      fill_rect(x - 1, y - 1, d + 2, d + 2)
    x = x + d

#  main part
def gprintm():

#  colour parettes
  colour = []
  colour = colour + [ ( 32,  30,  22) ]
  colour = colour + [ ( 93,  94,  86) ] + [ ( 51,  69,  71) ] + [ ( 77,  52,  30) ]
  colour = colour + [ (111, 146, 156) ] + [ ( 94, 121, 131) ] + [ (173, 199, 205) ]
  colour = colour + [ (228, 229, 222) ] + [ (163, 160, 155) ] + [ (172, 138, 110) ]
  colour = colour + [ (153, 113,  87) ] + [ (210, 173, 158) ] + [ (200, 150, 119) ]
  colour = colour + [ (223, 201, 180) ] + [ ( 98,  76,  50) ] + [ (144,  93,  56) ]

#  colour code 
  gdata = [
   '000000012324445205444467526677846777425466444541122200214444467776645000445' , 
   '000000084114445505644467226777846666405666444555122000214114667776445002465' , 
   '00000091A845444504444466524777446667405467454555122000214444777677445002445' , 
   '000000432664466525645466554777446676404476456444112202111118667776442002445' , 
   '00000012046676640544446752667784666760546664688B88BC88DB6954777776442002645' , 
   '00100012246677640564446742477744666762546768D6DB8BBBBCBDDDB8667777642002645' , 
   '0022011221666774254444664247776566666546D698DBD77DDD77DD8D78886777645002445' , 
   '00200522224677642444446742477764667767777BEE8BB77D777777DBB7644666445002465' , 
   '2332252322567764054444674267776467777777745399D777D777777DB8D68488641202645' , 
   '3E2025002E5467742244446742467784677777771B828BD7D77D7777DDD8968886684002442' , 
   '2E30220302114774226444676267776BBD77777B8123BDB67D7777777DD8589487766502645' , 
   '322312020222477425444466424777BBBDD7777B8308BBD7DDDD7777DDC9911EAD777B55445' , 
   '323212030112567422444466424777BBD77777D89EA8BDDBDDDDD7D7DB9891AA99B77768645' , 
   '2302100222242674225555468256DBBB77777777B86BBBBDDD6BDDDDB8888596D899D776645' , 
   '3222100202565464224444666058B7BBBD777777DBDBDBBDBBBBBBBB8888888D77D89877645' , 
   'E32110020E264266224554676286BBBBDBD77BDD8BBD6BD6DBB88BB88CAA888D777D8967745' , 
   'E222E0020E16826622445546B4BA8BBBBB9BBCB98BBBBBBBBB8B8B989BA195BD7777789D7D6' , 
   '3222200E0228656620445466BBAABBBBBBA9AA89BBBB6BBBD88BBBB989AA9AB7DD777DB8777' , 
   '202010020114744422445866B9ACBBBBBCAAB8B89BBBBBA8BBBBB8BCC9AA9ABDDDD7777B877' , 
   'E22210020218764422444888BCACBBBBBCABBBB8B595BB9188BBBB888A19A8BB98DD7777B8D' , 
   'E20212020E28765422444DBBBBAABBBDBBBBDBBBCA851BBAA8B8BB8C9AA9A8BAA9DDD7777DD' , 
   '2022E0000228774550448DBBBBAABBBBBBBBBBBB91B82ABB1BB8BC9C9A99199AF989D77777D' , 
   '22321002211477655245BDDBBBCCABBBBBBBBBBBB14129B8F98B8B989A9F9AAAE999DDDDD77' , 
   '222220020114676450448DDBBBCCCABDBBBBBBBB812238BBAA8B99CA999E91A1FA99B9DD677' , 
   '222EE00301247774525486DBDBBCCABBDDDBDBBBB5103BBBAAB8999CA1AAEEA11AA9C9CD8DD' , 
   '323222002229777652445DDBBBBBCBBBDBBDBDBBBA1E1B8BAA9CC999A9AAEEAE1AA9A988DDD' , 
   '212220020E156776554448BBBBDDBDDDDDBBBBBBB95AABBB998C999119A1EF1E1FA9F9988DB' , 
   '1112200522E577774446488DDDDBBDBBBBDBBBBBBCB9BCCC9C9999AEF91EE11E11AAE999CC9' , 
   '21125200022167674445466BBDDBDDDBBBBBBBBBCCCCBBB89CC99AEE19E0E1E1EFAE1A998B8' , 
   '151E12000144666654812246BDBDDBDBBBBBBBBCBCC8CCC998CAAFEEAAE3EEE11FE21A599CC' , 
   '151222000224666686DD7641CDBDDDBDBBBCCBCCB99CCB8C8CAAEE3191321EE1FEEEFAA998C' , 
   '1122E200000224686DD77777ABBBDBBBBBBBCCCC99C89C9CCAFEEE319E33E1FE1E2E11AA9C8' , 
   '21E2E2000112039DDDD7777DCCCDBBDBBBC8CC9C99C9C8CC9F133E3AA332EEE1EEEEEEAAA99' , 
   '212222200111199CDD77D77DCCBBBDDBBBBCC9C99C9C9CBAA133E3EA323EEEEEEEE1EF1A199' , 
   'E22E2E200221999B7D7D77DCBCCDBBBBBB9999AA9AA999A1E33333AF0333EEE1EEE1EFAA199' , 
   '11223200022289CD77DD77CCCCCDBBBCCCC9999C9999A12E33003FA003E22E1EEE1E211AF99' , 
   '222322200221CCDDDDDDDDDCCCCBBBDBB99A98C9A9AEE3030300FA0033E23E1EEE1E2F1F199' , 
   '32020230022ACDDDCCBBCCCACCCCCDBCCCAAAA9AAA1EF3300303F30330333113EEE3E11A19A' , 
   '022002000EABDDD9FCCACFFFCCBCBCCCCAAAF1A58AAAA133303F300330322EE3EEE22EA1F9A' , 
   '302000001B7DDDCCCCAC9FFFFCCCCCCAAAAFAF1ABAB33A1103E300303203E1332EE2E1AE19A' , 
   '00000018DDDDDDC9CFFFFFEEF33EF3FFFFEFEEEEA3193FB9F330033003333303EEE23EF1FA1' , 
   '00001BDDDDDC9CA9FFFFEEE3333333EE1FA1FFAFA1F13EFA3333333303030003E1E0EEA119A' , 
   '0E9DDD7DBCFCA9FFFFEF333FE33FF9AFAFE33333EF1E1E33E333303003030003EA10EE1EA9A' , 
   '8DD7DDCCFCFAFFFFFEE33FF33FAA9FFF3303330300003F11EE33300000000003FAE03EEAF9A' , 
   'DDCCCFCFACFFFEEFFEFFFFFFCCFFFFE303FCFFE3000000003000000000000000AAE2EE1F19F' , 
   'CFCCAACAAFFFFFFF3FFA9CCFA33F9F33F9CAAFF3300000000000000000000000FA122EF1F9A' , 
   'FCFFCFFFFEFFFFFFACAAFFFAF3FCA33ACCAAAFFF330000000000000000000000E99E2EF119A' , 
   'FFCFFFFFEFFFAFCCFFFEFCCA3FCCF3ACCAACAAFFF33000000000000000000000E98EEE11AAA' , 
   'CCFFFEF3FFFFCCFFFFACCCAFFCCF3ACC9CCAAC9BAFF300000000000000000000EFCAF3A3F9A' , 
   'FFFFFFFFFFCCFFFFACCCCCF3FC9FFCBCCCCBBDD77DBA30000000000000000000EFC9EEFEA99' 
  ]

  d = 4   # pixel size
  x = 10  # picture x coords
  y = 10  # picture y coords

  pf = getplatform()
#  pf :
#       -1 = non support
#        0 = Casio fx-CG50
#        1 = Numworks
#        2 = TI-84 Plus CE Python
#        3 = HP Prime non cas

  if pf == -1:
    print('non support')
  if pf == 2:    #  TI-84 Plus CE Python
  	clear()
  if pf == 3:    #  HP Prime non cas
  	fill_rect(0, 0, 320, 222, (224, 240, 200))
  if pf != -1:
    for st in gdata:
      gprint(pf, colour, x, y, d, st)
      y = y + d
  if pf == 0:    #  Casio fx-CG59
    show_screen() 
  if pf == 1:  #  Numworks
    pass
  if pf == 2:  #  TI-84 Plus CE Python
    show_draw()

gprintm()

#  for HP Prime non cas
#end

export gprint3m()
begin
  gprintm0();
  wait
end;