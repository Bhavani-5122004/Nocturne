import sqlite3
from flask import Flask, render_template, request, url_for, redirect

while True:
    
    
    self = sqlite3.connect('playlist.db',check_same_thread=False)
    cursor = self.cursor()
    try:
       
        
        app = Flask(__name__)
        app.static_folder = '.'
        app.template_folder='.'
        
        @app.route('/')
        def playlist():
            query = 'CREATE TABLE IF NOT EXISTS SONGS (SONG_ID CHAR(4),SONG_NAME CHAR(60),ARTIST CHAR(20),DURATION CHAR(4));'
            cursor.execute(query)
            query = 'CREATE TABLE IF NOT EXISTS PLAYLIST (SONG_NAME CHAR(60),ARTIST CHAR(20),DURATION CHAR(4));'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU1","Between Us","Little Mix","3:39");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU2","DNA","Little Mix","3:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU3","Wings","Little Mix","3:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU4","Move","Little Mix","3:53");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU5","Salute","Little Mix","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU6","Black Magic","Little Mix","3:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU7","Hair","Little Mix","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU8","Touch","Little Mix","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU9","No More Sad Songs","Little Mix","3:45");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU10","Power","Little Mix","4:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU11","Woman Like Me","Little Mix","3:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU12","Break Up Song","Little Mix","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU13","Confetti","Little Mix","3:05");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU14","Sweet Melody","Little Mix","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BU15","Heartbreak Anthem","Little Mix","3:03");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF2","Holiday","Little Mix","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF5","Happiness","Little Mix","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF6","Not A Pop Song","Little Mix","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF7","Nothing But My Feelings","Little Mix","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF8","Gloves Up","Little Mix","2:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF9","A Mess (Happy 4 U)","Little Mix","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF10","""My Love Won\'t Let You Down""","Little Mix","2:54");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF11","Rendezvous","Little Mix","2:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF12","If You Want My Love","Little Mix","2:40");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CF13","Breathe","Little Mix","3:29");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM1","The National Manthem","Little Mix","0:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM3","Think About Us","Little Mix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM4","Strip (feat. Sharaya J)","Little Mix","3:19");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM5","Monster In Me","Little Mix","3:45");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM6","Joan of Arc","Little Mix","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM7","Love A Girl Right","Little Mix","3:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM8","American Boy","Little Mix","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM9","Told You So","Little Mix","3:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM10","Wasabi","Little Mix","2:34");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM11","More Than Words (feat. KAMILLE)","Little Mix","3:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM12","Motivate","Little Mix","3:21");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM13","Notice","Little Mix","3:34");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM14","The Cure","Little Mix","3:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM15","Forget You Not","Little Mix","3:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM16","Woman\'s World","Little Mix","3:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM17","The Cure(Stripped)","Little Mix","1:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LM18","Only You","Little Mix","3:09");'
            cursor.execute(query)
            

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD2","Touch (feat. Kid Ink)","Little Mix","3:22");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD3","Reggaetón Lento (Remix)","Little Mix","3:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD4","F.U.","Little Mix","3:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD5","Power(feat. Stormzy)","Little Mix","4:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD6","No More Sad Songs(feat. Machine Gun Kelly)","Little Mix","3:45");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD7","Oops(feat. Charlie Puth)","Little Mix","3:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD8","You Gotta Not","Little Mix","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD9","Down & Dirty","Little Mix","2:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD10","Your Love","Little Mix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD11","Nobody Like You","Little Mix","4:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD12","Private Show","Little Mix","2:41");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD13","Nothing Else Matters","Little Mix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD14","If I Get My Way","Little Mix","3:40");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD15","Is Your Love Enough","Little Mix","3:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD16","Dear Lover","Little Mix","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD20","Beep Beep","Little Mix","3:52");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GD21","Freak","Little Mix","3:36");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW2","Love Me Like You","Little Mix","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW3","Weird People","Little Mix","3:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW4","Secret Love Song (feat. Jason Derulo)","Little Mix","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW6","Grown","Little Mix","2:36");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW7","I Love You","Little Mix","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW8","OMG","Little Mix","3:23");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW9","Lightning","Little Mix","5:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW10","A.D.I.D.A.S","Little Mix","3:22");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW11","Love Me or Leave Me","Little Mix","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW12","The End","Little Mix","2:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW13","I Won\'t","Little Mix","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW14","Secret Love Song Pt. II","Little Mix","4:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW15","Clued Up","Little Mix","4:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW16","The Beginning","Little Mix","1:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW17","Hair (feat. Sean Paul)","Little Mix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("GW18","Hair (feat. Sean Paul) -Wideboys Remix","Little Mix","3:48");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL3","Little Me","Little Mix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL4","Word Up!","Little Mix","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL5","Nothing Feels Like You","Little Mix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL6","Towers","Little Mix","3:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL7","Competition","Little Mix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL8","These Four Walls","Little Mix","3:28");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL9","About the Boy","Little Mix","3:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL10","Boy","Little Mix","2:54");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL11","Good Enough","Little Mix","3:52");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL12","Mr. Loverboy","Little Mix","3:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL13","A Different Beat","Little Mix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL14","See Me Now","Little Mix","3:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL15","They Just Don\'t Know You","Little Mix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SL16","Stand Down","Little Mix","3:39");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW1","Mauja Hi Mauja","Pritam","4:05");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW2","Tum Se Hi","Pritam","5:21");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW3","Yeh Ishq Hai","Pritam","4:40");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW4","Nagada Nagada","Pritam","3:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW5","Aao Milo Chalo","Pritam","5:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW6","Aaoge Jab Tum","Pritam","5:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW7","Tum Se Hi (Remix)","Pritam","4:22");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW8","Yeh Ishq Hai (Remix)","Pritam","4:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW9","Mauja Hi Mauja (Remix)","Pritam","4:28");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("JW10","Tum Se Hi (Instrumental)","Pritam","4:54");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ1","Badtameex Dil","Pritam","4:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ2","Balam Pichkari","Pritam","4:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ3","Ilahi","Pritam","3:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ4","Kabira","Pritam","3:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ5","Dilliwali Girlfriend","Pritam","4:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ6","Subhanallah","Pritam","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ7","Ghaghra","Pritam","5:04");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ8","Kabira (Encore)","Pritam","4:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("YJ9","Illahi(Repires)","Pritam","3:34");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU1","Pee Loon","Pritam","4:45");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU2","Tum Jo Aaye","Pritam","4:46");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU3","I Am In Love","Pritam","4:59");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU4","Parda","Pritam","5:21");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU5","Babu Rao","Pritam","4:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU6","Tum Jo Aaye (Remix)","Pritam","4:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU8","Pee Loon (Remix)","Pritam","4:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU9","I Am In Love (Dance)","Pritam","2:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("OU10","I Am In Love (Female)","Pritam","1:44");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT1","Tum Hi Ho Bandhu","Pritam","4:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT2","Daru Desi","Pritam","4:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT3","Yaariyan - Male Vocals","Pritam","6:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT4","Second Hand Jawaani","Pritam","4:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT5","Tera Naam Japdi Phira","Pritam","3:39");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT6","Luttna","Pritam","5:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT7","Jugni","Pritam","6:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT8","Yaariyan - Female Vocals","Pritam","4:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT9","Luttna - Reprise","Pritam","4:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT10","Tera Naam Japdi Phira - Remix","Pritam","4:10");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CT11","Main Sharaabi","Pritam","4:25");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD1","Ae Dil Hai Mushkil","Pritam","4:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD2","Bulleya","Pritam","5:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD3","Channa Mereya","Pritam","4:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD4","The Break Up Song","Pritam","4:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD5","Cutiepie","Pritam","3:51");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD6","Alizeh","Pritam","4:42");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD7","Bulleya - Reprise","Pritam","5:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD8","Channa Mereya - Unplugged","Pritam","2:45");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AD9","Aaj Jaane Ki Zid Na Karo","Pritam","2:51");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV1","I\'ll Do The Talking Tonight","Pritam","4:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV2","Dil Mura Muft Ka","Pritam","4:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV3","Raabta (Siyaah Remix)","Pritam","4:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV4","Pungi","Pritam","4:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV5","Agent Vinod (Theme)","Pritam","4:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV6","I\'ll Do The Talking Tonight (Remix)","Pritam","4:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV7","Raabta(Night In A Motel)","Pritam","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV8","Pungi (Remix)","Pritam","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV9","Raabta","Pritam","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV10","Dil Mura Muft Ka (Remix)","Pritam","3:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV11","Raabta (Kehte Hain Khudah Ne)","Pritam","4:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AV12","Gobind Bolo","Pritam","1:56");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST1","Circles","Seventeen","3:59");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST2","_WORLD","Seventeen","2:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST3","Fallin\' Flower (Korean Ver.)","Seventeen","3:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST4","Cheers","Seventeen","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST5","Darl+ing","Seventeen","2:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST6","HOT","Seventeen","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST7","Don Quixote","Seventeen","2:52");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST8","March","Seventeen","3:16");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST9","Domino","Seventeen","3:34");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST10","Shadow","Seventeen","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST11","\'bout you","Seventeen","2:24");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST12","IF you leave me","Seventeen","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("ST13","Ash","Seventeen","3:21");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT1","To You","Seventeen","3:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT2","Rock With You","Seventeen","3:00");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT3","Crush","Seventeen","2:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT4","PANG!","Seventeen","2:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT5","Imperfect Love","Seventeen","3:24");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT6","I Can\'t Run Away","Seventeen","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT7","2 Minus 1 (Bonus Track)","Seventeen","3:10");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO1","HIT","Seventeen","3:23");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO2","Lie Again","Seventeen","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO3","Fear","Seventeen","2:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO4","Let Me Hear You Say","Seventeen","3:00");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO5","247","Seventeen","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO6","Second Life","Seventeen","3:22");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO7","Network Love","Seventeen","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO8","Back It Up","Seventeen","3:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO9","Lucky","Seventeen","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO10","Snapshoot","Seventeen","2:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AO11","Happy Ending (Korean Ver.)","Seventeen","3:28");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA1","Intro. New World","Seventeen","0:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA2","CHANGE UP","Seventeen","3:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA3","Without You","Seventeen","3:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA4","Clap","Seventeen","2:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA5","Bring It","Seventeen","3:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA6","Lilli Yabbay","Seventeen","3:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA7","TRAUMA","Seventeen","3:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA8","Pinwheel","Seventeen","s:s9");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA9","Flower","Seventeen","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA10","Rocket","Seventeen","3:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA11","Hello","Seventeen","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA12","Campfire","Seventeen","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TA13","Outro. Incompletion","Seventeen","1:17");'
            cursor.execute(query)

            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL1","Chuck","Seventeen","2:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL2","Pretty U","Seventeen","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL3","Still Lonely","Seventeen","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL4","Hit Song","Seventeen","3:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL5","Say Yes","Seventeen","3:50");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL6","Drift Away","Seventeen","3:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL7","Adore U (Vocal Team Ver.)","Seventeen","3:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL8","Monday To Saturday (Hiphop Team Ver.)","Seventeen","3:23");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL9","Shining Diamond (Performace Team Ver.)","Seventeen","2:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("LL10","Love Letter","Seventeen","2:58");'
            cursor.execute(query)
            
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT1","Fake & True","Twice","3:39");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT2","Stronger","Twice","3:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT3","Breakthrough","Twice","3:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT4","Changing!","Twice","3:42");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT5","HAPPY HAPPY","Twice","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT6","What You Waiting For","Twice","3:21");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT7","Be OK","Twice","3:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT8","POLISH","Twice","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT9","How u doin\'","Twice","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AT10","The Reason Why","Twice","3:46");'
            cursor.execute(query)





            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO1","Talk That Talk","Twice","2:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO2","Queen Of Hearts","Twice","3:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO3","Basics","Twice","2:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO4","Trouble","Twice","3:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO5","Brave","Twice","3:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO6","Gone","Twice","3:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("BO7","When We Were Kids","Twice","3:09");'
            cursor.execute(query)





            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS1","Feel Special","Twice","3:36");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS2","RAINBOW","Twice","2:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS3","GET LOUD","Twice","3:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS4","TRICK IT","Twice","3:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS5","LOVE FOOLISH","Twice","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS6","21:29","Twice","3:48");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FS7","BREAKTHROUGH","Twice","3:37");'
            cursor.execute(query)







            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL1","SCIENTIST","Twice","3:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL2","MOONLIGHT","Twice","3:39");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL3","ICON","Twice","2:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL4","CRUEL","Twice","3:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL5","REAL YOU","Twice","3:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL6","F.I.L.A","Twice","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL7","LAST WALTZ","Twice","2:50");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL8","ESPRESSO","Twice","3:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL9","REWIND","Twice","3:00");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL10","CACTUS","Twice","3:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL11","PUSH & PULL","Twice","3:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL12","HELLO","Twice","3:03");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL13","1,3,2","Twice","3:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL14","CANDY","Twice","3:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("FL15","The Feels","Twice","3:18");'
            cursor.execute(query)





            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW1","Perfect World","Twice","3:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW2","BETTER","Twice","3:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW3","Good At Love","Twice","3:51");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW4","Fanfare","Twice","3:40");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW5","Kura Kura","Twice","3:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW6","Four-leaf Clover","Twice","3:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW7","In the summer","Twice","3:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW8","PIECES OF LOVE","Twice","4:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW9","Thank you, Family","Twice","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PW10","PROMISE","Twice","4:19");'
            cursor.execute(query)







            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT1","SET ME FREE","Twice","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT2","MOONLIGHT SUNRISE","Twice","3:00");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT3","GOT THE THRILLS","Twice","2:53");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT4","BLAME IT ON ME","Twice","2:56");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT5","WALLFLOWER","Twice","2:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("RT6","CRAZY STUPID LOVE","Twice","3:01");'
            cursor.execute(query)








            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP1","O Come, All Ye Faithful","Pentatonix","3:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP2","God Rest Ye Merry Gentlemen","Pentatonix","2:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP3","White Christmas","Pentatonix","3:19");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP4","I\'ll Be Home for Christmas","Pentatonix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP5","Up on the Housetop","Pentatonix","2:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP6","The Christmas Sing-Along","Pentatonix","3:16");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP7","Coventry Carol","Pentatonix","3:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP8","Hallelujah","Pentatonix","4:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP9","Coldest Winter","Pentatonix","2:28");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP10","Good to Be Bad","Pentatonix","2:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AP11","Merry Christmas, Happy Holidays","Pentatonix","3:57");'
            cursor.execute(query)



            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH1","Home","Pentatonix","2:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH2","When The Party\'s Over","Pentatonix","3:11");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH3","Blinding Lights","Pentatonix","3:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH4","Break My Heart","Pentatonix","3:38");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH5","Cologne","Pentatonix","3:04");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("AH6","Dreams","Pentatonix","2:57");'
            cursor.execute(query)




            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG1","It\'s Been A Long, Long Time","Pentatonix","2:07");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG2","Wonderful Christmastime","Pentatonix","2:31");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG3","I Saw Three Ships","Pentatonix","3:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG4","Home for the Holidays","Pentatonix","2:36");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG5","River","Pentatonix","2:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG6","Over the River","Pentatonix","2:39");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG7","Evergreen","Pentatonix","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG8","Frosty the Snowman","Pentatonix","2:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG9","I Just Called to Say I Love You","Pentatonix","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG10","Little Saint Nick","Pentatonix","2:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG11","It Came Upon the Midnight Clear","Pentatonix","3:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG12","My Heart With You","Pentatonix","4:33");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG13","The Prayer","Pentatonix","4:21");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EG14","We Wish You A Merry Christmas","Pentatonix","2:16");'
            cursor.execute(query)



            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX1","Papaoutai","Pentatonix","4:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX2","On My Way Home","Pentatonix","3:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX3","La La Latch","Pentatonix","3:41");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX4","See Through","Pentatonix","3:19");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX5","Standing By","Pentatonix","4:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX6","Can\'t Hold Us","Pentatonix","3:17");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX7","Royals","Pentatonix","3:50");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX8","Somebody That I Used To Know","Pentatonix","2:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX9","Radioactive","Pentatonix","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PX10","Say Something","Pentatonix","4:31");'
            cursor.execute(query)



            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT1","Can\'t Hold Us","Pentatonix","3:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT2","Natural Disaster","Pentatonix","3:30");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT3","Valentine","Pentatonix","2:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT4","Hit the Road Jack","Pentatonix","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT5","Run To You","Pentatonix","2:52");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT6","I Need Your Love","Pentatonix","4:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT7","Daft Punk","Pentatonix","4:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT8","Save The World","Pentatonix","3:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("PT9","Love Again","Pentatonix","3:18");'
            cursor.execute(query)




            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL1","Happy Now","Pentatonix","3:26");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL2","Love Me When I Don\'t","Pentatonix","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL3","Coffee In Bed","Pentatonix","3:15");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL4","Be My Eyes","Pentatonix","3:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL5","A Little Space","Pentatonix","2:54");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL6","Side","Pentatonix","3:27");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL7","Bored","Pentatonix","2:47");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL8","Exit Signs","Pentatonix","3:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL9","Never Gonna Cry Again","Pentatonix","2:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL10","The Lucky Ones","Pentatonix","3:10");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("TL11","It\'s Different Now","Pentatonix","3:37");'
            cursor.execute(query)






            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL1","Clouds","Sabrina Carpenter","3:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL2","Fix Me Up","Sabrina Carpenter","4:38");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL3","My Little Dancer","Sabrina Carpenter","3:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL4","Galaxies","Sabrina Carpenter","4:28");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL5","Blueberries","Sabrina Carpenter","2:23");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("CL6","How To Go To Confession","Sabrina Carpenter","3:07");'
            cursor.execute(query)








            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI1","emails i can\'t send","Sabrina Carpenter","1:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI2","Vicious","Sabrina Carpenter","2:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI3","Read Your Mind","Sabrina Carpenter","3:37");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI4","Tornado Warnings","Sabrina Carpenter","3:24");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI5","because i liked a boy","Sabrina Carpenter","3:16");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI6","Already Over","Sabrina Carpenter","2:50");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI7","how many things","Sabrina Carpenter","4:03");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI8","bet u wanna","Sabrina Carpenter","2:43");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI9","Nonsense","Sabrina Carpenter","2:54");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI10","Fast Times","Sabrina Carpenter","2:54");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI11","skinny dipping","Sabrina Carpenter","2:57");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI12","Bad For Business","Sabrina Carpenter","3:08");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EI13","decode","Sabrina Carpenter","3:08");'
            cursor.execute(query)





            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV1","On Purpose","Sabrina Carpenter","3:58");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV2","Feels Like Lonliness","Sabrina Carpenter","3:20");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV3","Thumbs","Sabrina Carpenter","3:36");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV4","No Words","Sabrina Carpenter","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV5","Run And Hide","Sabrina Carpenter","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV6","All We Have Is Love","Sabrina Carpenter","3:02");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV7","Mirage","Sabrina Carpenter","3:25");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV8","Don\'t Want It Back","Sabrina Carpenter","3:01");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV9","Shadows","Sabrina Carpenter","2:582");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EV10","Space","Sabrina Carpenter","3:06");'
            cursor.execute(query)






            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO1","Eyes Wide Open","Sabrina Carpenter","3:12");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO2","Can\'t Blame A Girl For Trying","Sabrina Carpenter","2:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO3","The Middle Of Starting Over","Sabrina Carpenter","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO4","We\'ll Be The Stars","Sabrina Carpenter","3:06");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO5","Two Young Hearts","Sabrina Carpenter","3:53");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO6","Your Love\'s Like","Sabrina Carpenter","3:29");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO7","Too Young","Sabrina Carpenter","3:14");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO8","Seamless","Sabrina Carpenter","4:16");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO9","Right Now","Sabrina Carpenter","3:35");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO10","Darling I\'m A Mess","Sabrina Carpenter","2:59");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO11","White Flag","Sabrina Carpenter","3:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("EO12","Best Thing I Got","Sabrina Carpenter","3:19");'
            cursor.execute(query)








            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO1","Almost Love","Sabrina Carpenter","3:32");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO2","Paris","Sabrina Carpenter","3:38");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO3","Hold Tight","Sabrina Carpenter","2:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO4","Sue Me","Sabrina Carpenter","2:59");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO5","prfct","Sabrina Carpenter","2:46");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO6","Bad Time","Sabrina Carpenter","3:04");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO7","Mona Lisa","Sabrina Carpenter","2:18");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SO8","Diamonds Are Forever","Sabrina Carpenter","3:49");'
            cursor.execute(query)





            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA1","In My Bed","Sabrina Carpenter","3:09");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA2","Pushing 20","Sabrina Carpenter","2:46");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA3","Can\'t Stop Me","Sabrina Carpenter","3:42");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA4","I\'m Fakin","Sabrina Carpenter","2:55");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA5","Take Off All Your Cool","Sabrina Carpenter","3:03");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA6","Tell Em","Sabrina Carpenter","4:40");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA7","Exhale","Sabrina Carpenter","2:44");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA8","Take You Back","Sabrina Carpenter","2:49");'
            cursor.execute(query)
            query = 'INSERT INTO SONGS (SONG_ID,SONG_NAME,ARTIST,DURATION) VALUES("SA9","Looking At Me","Sabrina Carpenter","3:01");'
            cursor.execute(query)
            
            query = 'SELECT SONG_NAME,ARTIST,DURATION FROM SONGS WHERE SONG_ID LIKE "EV%";'
            cursor.execute(query)
            result=cursor.fetchall()
            for i in result:
                print(i,"\n")
            
            
            query = 'SELECT * FROM PLAYLIST;'
            cursor.execute(query)
            result=cursor.fetchall()
            return render_template('playlist.html',result=result)
        
        i=0

        
        
        @app.route('/print_first_row',methods=['POST'])
        def print_first_row():
            global i
            column1 = request.form['column1']
            column2 = request.form['column2']
            column3 = request.form['column3']
            cursor.execute('SELECT EXISTS(SELECT * FROM PLAYLIST WHERE SONG_NAME=?)',[column1])
            result=cursor.fetchall()
            exists=0
            for i in result:
                if i!='[':
                    for j in i:
                        exists=int(j)
            print(exists)
            if exists==0:    
                cursor.execute("INSERT INTO PLAYLIST VALUES (?,?,?)",(column1,column2,column3))
                query = 'SELECT * FROM PLAYLIST;'
                cursor.execute(query)
                result=cursor.fetchall()
                return render_template('playlist.html',result=result)
            else:
                query = 'SELECT * FROM PLAYLIST;'
                cursor.execute(query)
                result=cursor.fetchall()
                return render_template('playlist.html',result=result)
                
        @app.route('/remove',methods=['POST'])
        def remove():
            global i
            column1 = request.form['column1']
            column2 = request.form['column2']
            column3 = request.form['column3']
            print(column1,column2,column3)
            cursor.execute('DELETE FROM PLAYLIST WHERE SONG_NAME=?',[column1])
            query = 'SELECT * FROM PLAYLIST;'
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            return render_template('playlist.html',result=result)

        @app.route('/artists')   
        def artists ():
            return render_template('artists.html')
        i=0
        
        @app.route('/lmbetweenus')   
        def lmbetweenus ():
            return render_template('lmbetweenus.html')

        @app.route('/home')   
        def home ():
            return render_template('home.html')

        @app.route('/lm')   
        def lm ():
            return render_template('lm.html')

        @app.route('/lmconfetti')   
        def lmconfetti ():
            return render_template('lmconfetti.html')

        @app.route('/lmgetweird')   
        def lmgetweird ():
            return render_template('lmgetweird.html')
        
        @app.route('/lmglorydays')   
        def lmglorydays ():
            return render_template('lmglorydays.html')

        @app.route('/lmlm5')   
        def lmlm5 ():
            return render_template('lmlm5.html')

        @app.route('/lmsalute')   
        def lmsalute ():
            return render_template('lmsalute.html')

        @app.route('/nocturne')   
        def nocturne ():
            return render_template('nocturne.html')

        @app.route('/pradhm')   
        def pradhm ():
            return render_template('pradhm.html')

        @app.route('/prav')   
        def prav ():
            return render_template('prav.html')


        @app.route('/prjwm')   
        def prjwm ():
            return render_template('prjwm.html')

        @app.route('/prc')   
        def prc ():
            return render_template('prc.html')

        @app.route('/pritam')   
        def pritam ():
            return render_template('pritam.html')

        @app.route('/prouatim')   
        def prouatim ():
            return render_template('prouatim.html')

        @app.route('/pryjhd')   
        def pryjhd ():
            return render_template('pryjhd.html')

        @app.route('/spotlight')   
        def spotlight ():
            return render_template('spotlight.html')

        @app.route('/svt')   
        def svt ():
            return render_template('svt.html')

        @app.route('/svtanode')   
        def svtanode ():
            return render_template('svtanode.html')

        @app.route('/svtat')   
        def svtat ():
            return render_template('svtat.html')

        @app.route('/svtfts')   
        def svtfts ():
            return render_template('svtfts.html')

        @app.route('/svtlal')   
        def svtlal ():
            return render_template('svtlal.html')

        @app.route('/svts17')   
        def svts17 ():
            return render_template('svts17.html')

        @app.route('/svtteenage')   
        def svtteenage ():
            return render_template('svtteenage.html')

        @app.route('/about')   
        def about ():
            return render_template('about.html')

        
        @app.route('/fol')   
        def fol ():
            return render_template('fol.html')

        @app.route('/theluckyones')   
        def theluckyones ():
            return render_template('theluckyones.html')

        @app.route('/pentatonix')   
        def pentatonix ():
            return render_template('pentatonix.html')

        @app.route('/twice')   
        def twice ():
            return render_template('twice.html')

        @app.route('/andtwice')   
        def andtwice ():
            return render_template('andtwice.html')

        @app.route('/apentatonixchristmas')   
        def apentatonixchristmas ():
            return render_template('apentatonixchristmas.html')

        @app.route('/perfectworld')   
        def perfectworld ():
            return render_template('perfectworld.html')

        @app.route('/ptx')   
        def ptx ():
            return render_template('ptx.html')

        @app.route('/athome')   
        def athome ():
            return render_template('athome.html')

        @app.route('/ptxvol2')   
        def ptxvol2 ():
            return render_template('ptxvol2.html')

        @app.route('/between1and2')   
        def between1and2 ():
            return render_template('between1and2.html')

        @app.route('/readytobe')   
        def readytobe ():
            return render_template('readytobe.html')

        @app.route('/clouds')   
        def clouds ():
            return render_template('clouds.html')

        @app.route('/emailsicantsend')   
        def emailsicantsend ():
            return render_template('emailsicantsend.html')

        @app.route('/evergreen')   
        def evergreen ():
            return render_template('evergreen.html')

        @app.route('/sabrinacarpenter')   
        def sabrinacarpenter ():
            return render_template('sabrinacarpenter.html')

        @app.route('/evolution')   
        def evolution ():
            return render_template('evolution.html')

        @app.route('/singularact1')   
        def singularact1 ():
            return render_template('singularact1.html')

        @app.route('/singularact2')   
        def singularact2 ():
            return render_template('singularact2.html')

        @app.route('/eyeswideopen')   
        def eyeswideopen ():
            return render_template('eyeswideopen.html')
        
        @app.route('/feelspecial')   
        def feelspecial ():
            return render_template('feelspecial.html')

        @app.route('/search')   
        def search ():
            return render_template('search.html')



        
        
        if __name__ == '__main__': 
           app.run(host='0.0.0.0')

     

    except sqlite3.Error as error:
        print('Error occurred - ', error)
     

    finally:
       
        if self:
            self.close()
