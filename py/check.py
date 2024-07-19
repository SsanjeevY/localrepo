import requests

def check_domains(domains):
    expired_domains = []
    for domain in domains:
        try:
            response = requests.get(f"https://{domain}")  # Adjust URL scheme if needed (http/https)
            if 'expired' in response.text.lower():
                expired_domains.append(domain)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {domain}: {e}")
    
    return expired_domains

# Example usage:
if __name__ == "__main__":
    domain_list = [
"krishnaenterprise.vasyerp.com","tranquilsupermart.vasyerp.com","easybazar.vasyerp.com","grocbuy.vasyerp.com","downtownmart.vasyerp.com","tranquilsupermartchennur.vasyerp.com","rainbowsupermarket.vasyerp.com","mccmart.vasyerp.com","balajijodhpurstore.vasyerp.com","asm.vasyerp.com","1mart.vasyerp.com","gg.vasyerp.com","se.vasyerp.com","smartbasket.vasyerp.com","pournamissignature.vasyerp.com","cyberwines.vasyerp.com","dhanlaxmienterprises.vasyerp.com","archanaprovision.vasyerp.com","jaibazarstore.vasyerp.com","wedoo.vasyerp.com","theteg.vasyerp.com","atc.vasyerp.com","alankarstores.vasyerp.com","7heavensupermarket.vasyerp.com","saisampurna.vasyerp.com","padmavathienterprises.vasyerp.com","rrmart.vasyerp.com","sbazarindiaprivateltd.vasyerp.com","gapstores.vasyerp.com","charishmasupermarket.vasyerp.com","avaniorganics.vasyerp.com","rcm.vasyerp.com","vsanddjconnectprivatelimited.vasyerp.com","mintmegamart.vasyerp.com","truebuymart.vasyerp.com","bbreads.vasyerp.com","arm.vasyerp.com","kannanstores.vasyerp.com","99bazaar.vasyerp.com","vbmart.vasyerp.com","manchikanti.vasyerp.com","lakshsuperma.vasyerp.com","simplefoodnutrition.vasyerp.com","vaishnavienterprises.vasyerp.com","himalayfrsh.vasyerp.com","vandanaenterprisebigmart.vasyerp.com","valueplus.vasyerp.com","nareshwholesalegrocerystore.vasyerp.com","bfresh.vasyerp.com","shubhamsalescorporation.vasyerp.com","buybuycart.vasyerp.com","welgatelifestyleopcpvtltd.vasyerp.com","sps.vasyerp.com","freshvegetablefruit.vasyerp.com","rohinipoint.vasyerp.com","temptationfoods.vasyerp.com","getondoor.vasyerp.com","avakriretailpvtltd.vasyerp.com","cmdquality1.vasyerp.com","sixten.vasyerp.com","truebidsolutionspvtltd.vasyerp.com","ricedesk.vasyerp.com","shrishyamsupermart.vasyerp.com","thamaniyainternationalpvtltd.vasyerp.com","jiffyretail.vasyerp.com","raapenterprises.vasyerp.com","msvishalgeneralstore.vasyerp.com","reejhessentials.vasyerp.com","mrudulsaigrandbazaar.vasyerp.com","rjkmarketing.vasyerp.com","baqala.vasyerp.com","sapnaenterprise.vasyerp.com","bhagyalaxmidairy.vasyerp.com","hariomsweetsvasyerpcom.vasyerp.com","swayambhu.vasyerp.com","smart0603.vasyerp.com","shreeranghandicraft.vasyerp.com","xyxx.vasyerp.com","namkeennvilla.vasyerp.com","oasis.vasyerp.com","justnuts.vasyerp.com","themashardwarestore77.vasyerp.com","cleverkenindustriespvtltd.vasyerp.com","shivnerifresh.vasyerp.com","rsep.vasyerp.com","citybazaarr.vasyerp.com","riganthony.vasyerp.com","seelainfratechprivatelimited.vasyerp.com","gogiagroceryking.vasyerp.com","promart.vasyerp.com","shreeranghandicraft.vasyerp.com","bvgmenswear.vasyerp.com","istoredirecttradingpvtltd.vasyerp.com","rnpr.vasyerp.com","upsilonofficial.vasyerp.com","rnprgnt.vasyerp.com","idyasnaturals.vasyerp.com","ganeshfertilizers.vasyerp.com","saatejventuri.vasyerp.com","gulmil.vasyerp.com","tulsiart.vasyerp.com","hersheinbox.vasyerp.com","sitatheindiannari.vasyerp.com","jampani.vasyerp.com","veggieswala.vasyerp.com","uniseoul.vasyerp.com","nibbanibbistore.vasyerp.com","shasthas.vasyerp.com","rajukosta.vasyerp.com","plumthegourmetstore.vasyerp.com","astrostores.vasyerp.com","kcretail.vasyerp.com","fabpaisleyindia.vasyerp.com","kmall.vasyerp.com","thepetpoint.vasyerp.com","wklife.vasyerp.com","jayalaxmistore.vasyerp.com","minime.vasyerp.com","sonacloth.vasyerp.com","seastoneproperty.vasyerp.com","staplestation.vasyerp.com","sritulsitrust.vasyerp.com","mahalaxmisupermart.vasyerp.com","aanganofkutch.vasyerp.com","dhavalbhavsar.vasyerp.com"
    ]
    
    expired_domains = check_domains(domain_list)
    
    print("Domains containing 'expired' in response:")
    for domain in expired_domains:
        print(domain)
