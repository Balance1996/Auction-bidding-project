#bidding-input and store player into dictionary

def validate_bid(bid_input):
    return bid_input.isdigit()

# Step 1–4: Collect bids
def collect_bid(bid_dict):
    while True:
        name = input("Enter your name: \n")
        bid_input = input("Enter your bid:\n ")
        if not validate_bid(bid_input):
             print("Invalid bid")
           
        else:
            bid_dict[name] = int(bid_input)
        more = input("Are there more bidders? (yes/no): ").lower()
        
        if more != "yes":
            break
    return bid_dict

def get_highestbidder(bid_dict):
    highest_bid=max(bid_dict.values())
    highest_bidder=[] #[name, for name, bid in bid_dict.items() if bid==highest_bid]
    for name,bid in bid_dict.items():
        if bid==highest_bid:
            highest_bidder.append(name)
            
    return highest_bid, highest_bidder

def resolve_ties(highest_bidder, bid_dict):
          while len(highest_bidder)>=2:
               print(f"The ties among bidders with usd{highest_bid} is:{' , '.join(highest_bidder)}")
               for name in highest_bidder:
                   print(f'Hello {name}. Please reenter bid.')
                   rebid = input("REEnter your bid:\n ")
                   bid_dict[name]=validate_bid(rebid)
                  
          return bid_dict
                   
                   
def main():
    bid_dict = {}

    bid_dict = collect_bid(bid_dict)

    highest_bid, highest_bidder = get_highestbidder(bid_dict)

    while len(highest_bidder) > 1:
        bid_dict = resolve_ties(highest_bid, highest_bidder, bid_dict)
        highest_bid, highest_bidder = get_highestbidder(bid_dict)

    print(f"The winner is {highest_bidder[0]} with {highest_bid}.")  
                
            
if __name__=="__main__":
    main()
                   
               
    
                
            
    

            
            
        
