import subprocess
import time

regions = [
    'singapore', 'china', 'sri-lanka', 'malaysia', 'cambodia', 'philippines', 'hong-kong', 'india', 'macao', 'indonesia',
    'jp-tokyo', 'jp-streaming-optimized', 'mongolia', 'au-brisbane', 'au-sydney', 'au-perth', 'au-adelaide',
    'australia-streaming-optimized', 'au-melbourne', 'nigeria', 'morocco', 'algeria', 'it-milano', 'it-streaming-optimized',
    'malta', 'es-valencia', 'es-madrid', 'uk-london', 'uk-streaming-optimized', 'uk-southampton', 'uk-manchester', 'monaco',
    'france', 'belgium', 'portugal', 'andorra', 'vietnam', 'nepal', 'croatia', 'cyprus', 'de-frankfurt', 'de-berlin',
    'bosnia-and-herzegovina', 'czech-republic', 'us-salt-lake-city', 'us-west', 'us-silicon-valley', 'us-honolulu',
    'us-las-vegas', 'us-california', 'us-west-streaming-optimized', 'us-alaska', 'us-mississippi', 'us-missouri',
    'us-wyoming', 'us-texas', 'us-south-dakota', 'us-louisiana', 'us-arkansas', 'us-kentucky', 'us-north-carolina',
    'us-north-dakota', 'us-denver', 'us-new-mexico', 'us-kansas', 'us-connecticut', 'us-alabama', 'us-chicago', 'us-indiana',
    'us-seattle', 'us-south-carolina', 'us-west-virginia', 'us-minnesota', 'us-washington-dc', 'us-tennessee', 'us-virginia',
    'us-idaho', 'us-nebraska', 'us-florida', 'us-michigan', 'us-pennsylvania', 'us-rhode-island', 'us-oklahoma', 'us-vermont',
    'us-east', 'us-maine', 'us-montana', 'us-new-hampshire', 'us-new-york', 'us-ohio', 'us-oregon', 'us-wisconsin', 'us-iowa',
    'us-atlanta', 'us-houston', 'us-east-streaming-optimized', 'us-wilmington', 'us-baltimore', 'us-massachusetts',
    'dk-streaming-optimized', 'dk-copenhagen', 'se-streaming-optimized', 'se-stockholm', 'austria', 'egypt',
    'north-macedonia', 'poland', 'turkey', 'fi-streaming-optimized', 'fi-helsinki', 'south-korea', 'norway', 'romania',
    'bulgaria', 'estonia', 'serbia', 'ireland', 'isle-of-man', 'luxembourg', 'united-arab-emirates', 'bangladesh',
    'saudi-arabia', 'slovenia', 'switzerland', 'iceland', 'latvia', 'panama', 'qatar', 'slovakia', 'lithuania', 'moldova',
    'ukraine', 'albania', 'greece', 'israel', 'ca-vancouver', 'ca-ontario', 'ca-montreal', 'ca-toronto', 'new-zealand',
    'greenland', 'south-africa', 'argentina', 'brazil', 'chile', 'ecuador', 'kazakhstan', 'liechtenstein', 'montenegro',
    'costa-rica', 'mexico', 'uruguay', 'bolivia', 'georgia', 'guatemala', 'peru', 'armenia', 'colombia', 'netherlands',
    'hungary', 'taiwan', 'bahamas', 'venezuela'
]



interval = 60 * 5

def change_region(region):
    command = f'piactl.exe set region {region}'

    subprocess.run(command, shell=True)

def connect_vpn():
    subprocess.run('piactl.exe connect', shell=True)

def disconnect_vpn():
    subprocess.run('piactl.exe disconnect', shell=True)

def main():
    try:
        while True:
            for region in regions:
                change_region(region)
                time.sleep(5)
                connect_vpn()
                time.sleep(5)
                disconnect_vpn()
    except KeyboardInterrupt:
        print("VPN Changer Terminated")

if __name__ == '__main__':
    main()



# piactl.exe set region -> loop
# piactl.exe connect 
# piactl.exe disconnect 




# piactl.exe monitor