# Import required libraries
import pandas as pd

loc= 'prediction.csv'


def predict_chance_to_win(suits, companion, power):
    
    df = pd.read_csv(loc) #load the csv
    
    # Filter rows on every characteristic 
    suit_df = df[df['Card Suit'] == suits]
    companion_df = df[df['Animal Name'] == companion]
    power_df = df[df['Fruit'] == power]

    # How much it have an effect on the total prob Example if heart is the most than if he choose heart the combined increase and so on  
    prob_suit = suit_df['Result'].mean() 
    prob_companion = companion_df['Result'].mean() 
    prob_power = power_df['Result'].mean() 
    
    # How many total feutures are repeated so it is based on that
    total_features = len(suit_df) + len(companion_df) + len(power_df)
    
    # Combine the probabilities using a weighted average and each feature's probability is weighted by how often it appears in the dataset
    combined_prob = ((len(suit_df) * prob_suit +len(companion_df) * prob_companion +len(power_df) * prob_power) / total_features
       
    )
    

    print(f"Card Suit ({suits}): {prob_suit:.2%}") #How much it have an effect 
    print(f"Animal Name ({companion}): {prob_companion:.2%}")
    print(f"Fruit ({power}): {prob_power:.2%}")
  
    return combined_prob * 100 #percentage


if __name__ == '__main__':
    # Choose 3 parameters for the game select one from each set of 5
    predicted_chance = predict_chance_to_win('Hearts', 'Lion', 'Mango')
    
    print(f"Predicted Chance to Win: {predicted_chance:.2f}%")
