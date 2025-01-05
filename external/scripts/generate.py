from external.user_interactions import generate_user_interactions
from external.user_metadata import generate_user_metadata

if __name__ == '__main__':

    # Generate sample datasets
    generate_user_interactions(1000000, '../user_interactions_sample.csv')
    generate_user_metadata(100000, '../user_metadata_sample.csv')

    print("Sample datasets generated successfully.")