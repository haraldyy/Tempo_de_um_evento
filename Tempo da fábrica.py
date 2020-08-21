def quantidade(tempo):
    segundo = int(tempo // 3600)
    minuto =int((tempo % 3600)// 60)
    hora =int((tempo % 3600) % 60)
    return (f'{segundo}:{minuto}:{hora}')

def main():
    tempo = int(input())
    tempot =quantidade(tempo)
    print(quantidade(tempo))

if __name__=='__main__':
    main()
