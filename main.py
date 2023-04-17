from pytube import YouTube

def indir(url):
    yt = YouTube(url)
    if yt.streams.filter(res='1080p', progressive=True, type='video').order_by('resolution').desc().first():
        yt = yt.streams.filter(res='1080p', progressive=True, type='video').order_by('resolution').desc().first()
    elif yt.streams.filter(res='720p', progressive=True, type='video').order_by('resolution').desc().first():
        yt = yt.streams.filter(res='720p', progressive=True, type='video').order_by('resolution').desc().first()
    elif yt.streams.filter(res='480p', progressive=True, type='video').order_by('resolution').desc().first():
        yt = yt.streams.filter(res='480p', progressive=True, type='video').order_by('resolution').desc().first()
    elif yt.streams.filter(res='360p', progressive=True, type='video').order_by('resolution').desc().first():
        yt = yt.streams.filter(res='360p', progressive=True, type='video').order_by('resolution').desc().first()

    try:
        yt.download()
        print(f'{yt.title} adlı video indirildi.')
    except:
        print("Bu video şu anda indirilemiyor, varsa sıradakine geçiliyor...")

print("URL'leri aralarına virgül koyarak giriniz !")
urls = input("URL'ler : ")

liste = urls.split(',')
for link in liste:
    indir(link.strip())








