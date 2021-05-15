class style():
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = "\033[0;32m"
    BLUE = '\033[34m'
    RESET = '\033[0m'
    MAGENTA = '\033[35m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    VOILET = '\33[36m'
    BOLD = '\033[1m'
    LIGHT_RED = '\033[1;31m'
    COLOR_BLACK="\033[0;30m"
    COLOR_RED="\033[0;31m"
    COLOR_GREEN="\033[0;32m"
    COLOR_BROWN="\033[0;33m"
    COLOR_BLUE="\033[0;34m"
    COLOR_PURPLE="\033[0;35m"
    COLOR_CYAN="\033[0;36m"
    LIGHT_WHITE = "\033[1;37m"
    COLOR_LIGHT_RED="\033[1;31m"
    COLOR_LIGHT_GREEN="\033[1;32m"
    COLOR_LIGHT_BLUE="\033[1;34m"
    COLOR_LIGHT_CYAN="\033[1;36m"
    COLOR_BOLD="\033[1m"
    COLOR_ITALIC="\033[3m"
    COLOR_BLINK="\033[5m"
    COLOR_NEGATIVE="\033[7m"
    COLOR_CROSSED="\033[9m"

port = {
    "7" :"Echo",
    "19" : "Chargen            ",      
    "20" : "FTP            ",
    "21" : "FTP            ",
    "22" : "SSH/SCP            ",
    "23" : "Telnet",
    "25" : "SMTP               ",
    "42" : "WINS Replication   ",
    "43" : "WHOIS              ",
    "49" : "TACACS             ",
    "53" : "DNS                ",
    "67" : "DHCP/BOOTP         ",
    "68" : "DHCP/BOOTP         ",
    "69" : "TFTP               ",
    "70" : "Gopher             ",
    "79" : "Finger       ",     
    "80" : "HTTP               ",
    "88" : "Kerberos           ",
    "102" : "MS Exchange       ",
    "110" : "POP3              ",
    "113" : "Ident",
    "119" : "NNTP (Usenet)     ",        
    "123" : "NTP               ",
    "135" : "Microsoft RPC     ",
    "137" : "NetBIOS           ",
    "138" : "NetBIOS           ",
    "139" : "NetBIOS           ",     
    "143" : "IMAP4             ",
    "161" : "SNMP              ",
    "162" : "SNMP              ",    
    "177" : "XDMCP             ",
    "179" : "BGP               ",
    "201" : "AppleTalk         ",
    "264" : "BGMP              ",
    "318" : "TSP               ",             
    "381" : "HP Openview       ",                  
    "383" : "HP Openview       ",
    "389" : "LDAP              ",     
    "411" : "Direct Connect    ",               
    "412" : "Direct Connect    ",       
    "443" : "HTTP over SSL     ",       
    "445" : "Microsoft DS      ",                    
    "464" : "Kerberos          ",
    "465" : "SMTP over SSL     ",
    "497" : "Retrospect        ",
    "500" : "ISAKMP            ",    
    "512" : "rexec             ",
    "513" : "rlogin            ", 
    "514" : "syslog            ",
    "515" : "LPD/LPR           ",           
    "520" : "RIP               ",
    "521" : "RIPng (IPv6)      ",
    "540" : "UUCP              ",
    "554" : "RTSP              ",    
    "546" : "DHCPv6            ",               
    "547" : "DHCPv6            ",       
    "560" : "rmonitor          ",                               
    "563" : "NNTP over SSL     ",                                           
    "587" : "SMTP              ",                                   
    "591" : "FileMaker         ",                 
    "593" : "Microsoft DCOM    ",               
    "631" : "Internet Printing ",                    
    "636" : "LDAP over SSL     ",                  
    "639" : "MSDP (PIM)        ",                  
    "646" : "LDP (MPLS)        ",                     
    "691" : "MS Exchange       ",                    
    "860" : "iSCSI             ",             
    "873" : "rsync             ",          
    "902" : "VMware Server     ",         
    "989" : "FTP over SSL      ",                    
    "990" : "FTP over SSL      ",           
    "993" : "IMAP4 over SSL    ",              
    "995" : "POP3 over SSL     ",      
    "1025" : "Microsoft RPC    ",                
    "1026" : "Windows Messenger",       
    "1029" : "Windows Messenger",    
    "1080" : "SOCKS Proxy      ",
    "1080" : "MyDoom           ",
    "1194" : "OpenVPN          ",
    "1214" : "Kazaa            ",         
    "1241" : "Nessus           ", 
    "1311" : "Dell OpenManage  ",                     
    "1337" : "WASTE            ",    
    "1433" : "Microsoft SQL    ",                 
    "1434" : "Microsoft SQL    ",            
    "1512" : "WINS             ",
    "1589" : "Cisco VQP        ",
    "1701" : "L2TP             ",
    "1723" : "MS PPTP          ",
    "1725" : "Steam            ",
    "1741" : "CiscoWorks 2000  ", 
    "1755" : "MS Media Server  ",
    "1812" : "RADIUS           ",
    "1813" : "RADIUS           ",
    "1863" : "MSN              ",
    "1985" : "Cisco HSRP       ",
    "2000" : "Cisco SCCP       ",
    "2002" : "Cisco ACS        ",
    "2049" : "NFS              ",
    "2082" : "cPanel           ",
    "2083" : "cPanel           ",
    "2100" : "Oracle XDB       ",
    "2222" : "DirectAdmin      ",
    "2302" : "Halo             ",
    "2483" : "Oracle DB        ",
    "2484" : "Oracle DB        ",
    "2745" : "Bagle.H          ",
    "2967" : "Symantec AV      ",
    "3050" : "Interbase DB     ",
    "3074" : "XBOX Live        ",
    "3124" : "HTTP Proxy       ",
    "3127" : "MyDoom           ",
    "3128" : "HTTP Proxy       ",
    "3222" : "GLBP             ",
    "3260" : "iSCSI Target     ",
    "3306" : "MySQL            ",
    "3389" : "Terminal Server  ",
    "3689" : "iTunes           ",
    "3690" : "Subversion       ",
    "3724" : "World of Warcraft",      
    "3784" : "Ventrilo         ", 
    "3785" : "Ventrilo         ",
    "4333" : "mSQL             ",
    "4444" : "Blaster          ",
    "4664" : "Google Desktop   ",       
    "4672" : "eMule            ",
    "4899" : "Radmin           ",
    "5000" : "UPnP             ",
    "5001" : "Slingbox         ",
    "5001" : "iperf            ",
    "5004" : "RTP              ",
    "5005" : "RTP              ",
    "5050" : "Yahoo! Messenger ",        
    "5060" : "SIP              ",
    "5190" : "AIM/ICQ          ",
    "5222" : "XMPP/Jabber      ",
    "5223" : "XMPP/Jabber      ",
    "5432" : "PostgreSQL       ",   
    "5500" : "VNC Server       ",
    "5554" : "Sasser           ",
    "5631" : "pcAnywhere       ",
    "5632" : "pcAnywhere       ",
    "5800" : "VNC over HTTP    ",
    "5900" : "VNC Server       ",
    "6000" : "X11              ",
    "6001" : "X11              ",
    "6112" : "Battle.net       ",
    "6129" : "DameWare         ",
    "6257" : "WinMX            ",
    "6346" : "Gnutella         ",
    "6347" : "Gnutella         ",
    "6500" : "GameSpy Arcade   ",
    "6566" : "SANE             ",
    "6588" : "AnalogX          ",
    "6665" : "IRC              ",
    "6666" : "IRC              ",
    "6667" : "IRC              ",
    "6668" : "IRC              ",
    "6669" : "IRC              ",
    "6679" : "IRC over SSL     ",
    "6697" : "IRC over SSL     ",
    "6699" : "Napster          ",
    "6881" :" BitTorrent  ",
    "6882" :" BitTorrent  ",
    "6883" :" BitTorrent  ",
    "6884" :" BitTorrent  ",
    "6885" :" BitTorrent  ",
    "6886" :" BitTorrent  ",
    "6887" :" BitTorrent  ",
    "6888" :" BitTorrent  ",
    "6889" :" BitTorrent  ",
    "6890" :" BitTorrent  ",
    "6891" :" BitTorrent  ",
    "6892" :" BitTorrent  ",
    "6893" :" BitTorrent  ",
    "6894" :" BitTorrent  ",
    "6895" :" BitTorrent  ",
    "6896" :" BitTorrent  ",
    "6897" :" BitTorrent  ",
    "6898" :" BitTorrent  ",
    "6899" :" BitTorrent  ",
    "6900" :" BitTorrent  ",
    "6901" :" BitTorrent  ",
    "6902" :" BitTorrent  ",
    "6903" :" BitTorrent  ",
    "6904" :" BitTorrent  ",
    "6905" :" BitTorrent  ",
    "6906" :" BitTorrent  ",
    "6907" :" BitTorrent  ",
    "6908" :" BitTorrent  ",
    "6909" :" BitTorrent  ",
    "6911" :" BitTorrent  ",
    "6912" :" BitTorrent  ",
    "6913" :" BitTorrent  ",
    "6914" :" BitTorrent  ",
    "6915" :" BitTorrent  ",
    "6916" :" BitTorrent  ",
    "6917" :" BitTorrent  ",
    "6918" :" BitTorrent  ",
    "6919" :" BitTorrent  ",
    "6920" :" BitTorrent  ",
    "6921" :" BitTorrent  ",
    "6922" :" BitTorrent  ",
    "6923" :" BitTorrent  ",
    "6924" :" BitTorrent  ",
    "6925" :" BitTorrent  ",
    "6926" :" BitTorrent  ",
    "6927" :" BitTorrent  ",
    "6928" :" BitTorrent  ",
    "6929" :" BitTorrent  ",
    "6930" :" BitTorrent  ",
    "6931" :" BitTorrent  ",
    "6932" :" BitTorrent  ",
    "6933" :" BitTorrent  ",
    "6934" :" BitTorrent  ",
    "6935" :" BitTorrent  ",
    "6936" :" BitTorrent  ",
    "6937" :" BitTorrent  ",
    "6938" :" BitTorrent  ",
    "6939" :" BitTorrent  ",
    "6941" :" BitTorrent  ",
    "6942" :" BitTorrent  ",
    "6943" :" BitTorrent  ",
    "6944" :" BitTorrent  ",
    "6945" :" BitTorrent  ",
    "6946" :" BitTorrent  ",
    "6947" :" BitTorrent  ",
    "6948" :" BitTorrent  ",
    "6949" :" BitTorrent  ",
    "6950" :" BitTorrent  ",
    "6951" :" BitTorrent  ",
    "6952" :" BitTorrent  ",
    "6953" :" BitTorrent  ",
    "6954" :" BitTorrent  ",
    "6955" :" BitTorrent  ",
    "6956" :" BitTorrent  ",
    "6957" :" BitTorrent  ",
    "6958" :" BitTorrent  ",
    "6959" :" BitTorrent  ",
    "6960" :" BitTorrent  ",
    "6961" :" BitTorrent  ",
    "6962" :" BitTorrent  ",
    "6963" :" BitTorrent  ",
    "6964" :" BitTorrent  ",
    "6965" :" BitTorrent  ",
    "6966" :" BitTorrent  ",
    "6967" :" BitTorrent  ",
    "6968" :" BitTorrent  ",
    "6969" :" BitTorrent  ",
    "6970" :" BitTorrent  ",
    "6971" :" BitTorrent  ",
    "6972" :" BitTorrent  ",
    "6973" :" BitTorrent  ",
    "6974" :" BitTorrent  ",
    "6975" :" BitTorrent  ",
    "6976" :" BitTorrent  ",
    "6977" :" BitTorrent  ",
    "6978" :" BitTorrent  ",
    "6979" :" BitTorrent  ",
    "6980" :" BitTorrent  ",
    "6981" :" BitTorrent  ",
    "6982" :" BitTorrent  ",
    "6983" :" BitTorrent  ",
    "6984" :" BitTorrent  ",
    "6985" :" BitTorrent  ",
    "6986" :" BitTorrent  ",
    "6987" :" BitTorrent  ",
    "6988" :" BitTorrent  ",
    "6989" :" BitTorrent  ",
    "6990" :" BitTorrent  ",
    "6991" :" BitTorrent  ",
    "6992" :" BitTorrent  ",
    "6993" :" BitTorrent  ",
    "6994" :" BitTorrent  ",
    "6995" :" BitTorrent  ",
    "6996" :" BitTorrent  ",
    "6997" :" BitTorrent  ",
    "6998" :" BitTorrent  ",
    "6999" : "BitTorrent  ",
    "6891" : "Windows Live     ",
    "6892" : "Windows Live     ",
    "6893" : "Windows Live     ",
    "6894" : "Windows Live     ",
    "6895" : "Windows Live     ",
    "6896" : "Windows Live     ",
    "6897" : "Windows Live     ",
    "6898" : "Windows Live     ",
    "6899" : "Windows Live     ",
    "6900" : "Windows Live     ",
    "6901" : "Windows Live     ",
    "6970" : "Quicktime        ",
    "7212" : "GhostSurf        ",
    "7648" : "CU-SeeMe         ",
    "7649" : "CU-SeeMe         ",
    "8000" : "Internet Radio   ",
    "8080" : "HTTP Proxy       ",
    "8086" : "Kaspersky AV     ",
    "8087" : "Kaspersky AV     ",
    "8118" : "Privoxy          ",
    "8200" : "VMware Server    ",
    "8500" : "Adobe ColdFusion ",
    "8767" : "TeamSpeak        ",
    "8866" : "Bagle.B          ",
    "9100" : "HP JetDirect     ",
    "9101" : "Bacula           ",
    "9103" : "Bacula           ",
    "9119" : "MXit             ",
    "9800" : "WebDAV           ",
    "9898" : "Dabber           ",
    "9988" : "Rbot/Spybot      ",
    "9999" : "Urchin           ",
    "10000" : "Webmin          ",
    "10000" : "BackupExec      ",
    "10113" : "NetIQ           ",
    "10116" : "NetIQ           ",
    "11371" : "OpenPGP         ",
    "12035" : "Second Life     ",
    "12036" : "Second Life     ",
    "12345" : "NetBus          ",
    "13720" : "NetBackup       ",
    "13721" : "NetBackup       ",
    "14567" : "Battlefield     ",
    "15118" : "Dipnet/Oddbob   ",
    "19226" : "AdminSecure     ",
    "19638" : "Ensim           ",
    "20000" : "Usermin         ",
    "24800" : "Synergy         ",
    "25999" : "Xfire           ",
    "27015" : "Half-Life       ",
    "27374" : "Sub7            ",
    "28960" : "Call of Duty    ",
    "31337" : "Back Orifice    ",
                        
}


chat = ["1863","5050","5190","5222","5223","6665","6666","6667","6668","6669","6679","6697","6891","6892","6893","6894","6895","6896","6897","6898","6899","6900","6901","7648","7649","8767","9119","25999",]

encrypted = ["22","443","465","500","563","636","989","990","993","995"]

gaming = ["1725","2302","3074","3724","6112","6500","12035","12036","14567","15118","27015""28960"]

malicious =["1080","2745","3127","4444","5554","9898","8866","9988","12345","31337"]

Peer_to_Pee =["411","412","1214","1337","4672","6257","6346","6347","6699","6881","6882","6883","6884","6885","6886","6887","6888","6889","6890","6891","6892","6893","6894","6895","6896","6897","6898","6899","6900","6901","6902","6903","6904","6905","6906","6907","6908","6909","6910","6911","6912","6913","6914","6915","6916","6917","6918","6919","6920","6921","6922","6923","6924","6925","6926","6927","6928","6929","6930","6931","6932","6933","6934","6935","6936","6937","6938","6939","6940","6941","6942","6943","6944","6945","6946","6947","6948","6949","6590","6951","6952","6953","6954","6955","6956","6957","6958","6959","6960","6961","6962","6963","6964","6965","6966","6967","6968","6969","6970","6971","6972","6973","6974","6975","6976","6977","6978","6979","6980","6981","6982","6983","6984","6985","6986","6987","6988","6989","6990","6991","6992","6993","6994","6995","6996","6997","6998","6999"]

streaming = ["1755","3784","3785","5001","5004","5005","5060","6970","8000","24800"]

print(style.COLOR_GREEN + style.BOLD + """
      .-------.     ,-----.    .-------. ,---------.               _______   .---.  .---.     .-''-.      _______   .--.   .--.      .-''-.  .-------.     
      \  _(`)_ \  .'  .-,  '.  |  _ _   \\          \             /   __  \  |   |  |_ _|   .'_ _   \    /   __  \  |  | _/  /     .'_ _   \ |  _ _   \    
      | (_ o._)| / ,-.|  \ _ \ | ( ' )  | `--.  ,---'            | ,_/  \__) |   |  ( ' )  / ( ` )   '  | ,_/  \__) | (`' ) /     / ( ` )   '| ( ' )  |    
      |  (_,_) /;  \  '_ /  | :|(_ o _) /    |   \  _ _    _ _ ,-./  )       |   '-(_{;}_). (_ o _)  |,-./  )       |(_ ()_)     . (_ o _)  ||(_ o _) /    
      |   '-.-' |  _`,/ \ _/  || (_,_).' __  :_ _: ( ' )--( ' )\  '_ '`)     |      (_,_) |  (_,_)___|\  '_ '`)     | (_,_)   __ |  (_,_)___|| (_,_).' __  
      |   |     : (  '\_/ \   ;|  |\ \  |  | (_I_)(_{;}_)(_{;}_)> (_)  )  __ | _ _--.   | '  \   .---. > (_)  )  __ |  |\ \  |  |'  \   .---.|  |\ \  |  | 
      |   |      \ `"/  \  ) / |  | \ `'   /(_(=)_)(_,_)--(_,_)(  .  .-'_/  )|( ' ) |   |  \  `-'    /(  .  .-'_/  )|  | \ `'   / \  `-'    /|  | \ `'   / 
      /   )       '. \_/``".'  |  |  \    /  (_I_)              `-'`-'     / (_{;}_)|   |   \       /  `-'`-'     / |  |  \    /   \       / |  |  \    /  
      `---'         '-----'    ''-'   `'-'   '---'                `._____.'  '(_,_) '---'    `'-..-'     `._____.'  `--'   `'-'     `'-..-'  ''-'   `'-'   
                """)

print(style.BOLD +style.MAGENTA + "Welcome To Our Port Services")

checker = input(style.BOLD + style.COLOR_LIGHT_BLUE +"Enter The Port Number:--" + style.GREEN) 

if checker in port:
    print("This Is Service Of "+ style.LIGHT_WHITE) 
else:
    print(style.LIGHT_RED + "This Port is Not Avalable Over Database Try Other Port"+ style.LIGHT_WHITE)

print( port.get(checker) )

if checker in chat:
    print(style.COLOR_PURPLE +"This Port Is Run In Chat Service" + style.LIGHT_WHITE)

if checker in encrypted:
    print(style.BLUE + "This Port Is Run In Encrypted Service" + style.LIGHT_WHITE)   

if checker in gaming:
    print(style.GREEN + "This Port Is Run In Gaming Service"+ style.LIGHT_WHITE)    

if checker in malicious:
    print(style.RED + "This Port Is Run In Malicious Service"+ style.LIGHT_WHITE)        

if checker in Peer_to_Pee:
    print(style.COLOR_CYAN + "This Port Is Run In Peer to Pee Services"+ style.LIGHT_WHITE)              

if checker in streaming:
    print(style.YELLOW + "This Port Is Run In Streaming Service"+ style.LIGHT_WHITE)             




