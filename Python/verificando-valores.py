#Variables
while True:
    try:
        String = input('Digite um texto interessante: ')
        if str(String):
            break
    except:
        print ('Você não digitou um texto.')
    finally:
        print ('Parabéns, seu texto é muito legal!')
        print (String)