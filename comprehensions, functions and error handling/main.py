from sqlalchemy import create_engine, text, inspect
import matplotlib.pyplot as plt
engine = create_engine("sqlite:///chinook.db")

'''with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM albums"))
    print(result.all())'''

def generate_bar_chart(labels, values):
    try:
        fig, ax = plt.subplots()
        fig.suptitle("Ammount of Tracks by Genre")
        ax.bar(labels, values)
        plt.xticks(rotation=90)
        plt.show()
    
    except Exception as e:
        print("An error has occurred, please check the data and try again")

def get_database_data():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT g.name, COUNT(g.GenreId) FROM tracks t INNER JOIN genres g ON t.GenreId = g.GenreId GROUP BY g.name ORDER BY 2")
            data = result.all()     
            labels = [x[0] for x in data]
            values = [y[1] for y in data]

            return labels, values
    except Exception as e:
        print("An error has occurred, please check the query and try again.")

def execute():
    labels, values = get_database_data()
    generate_bar_chart(labels, values)

if __name__ == "__main__":
    execute()



