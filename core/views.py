from django.shortcuts import render

def register(reqest):
    return render(reqest, 'register.html')



def main(reqest):
    return render(reqest, 'main.html')



def groups(reqest):
    return render(reqest, 'groups.html')




def news(reqest):
    return render(reqest, 'news.html')



def profile(reqest):
    return render(reqest, 'profile.html')