I started by learning some basic plot functions with Matplotlib. Having experience with python in the past, it was a relatively quick learn, and much easier to use compared to competitors like Seaborn or Plotly.

At the start of my code, I have a section that intends to load the dataset into VS. Due to some connection issue that my internet was having, I also implemented a manual load using the file on my laptop, that way I could consistently load the dataset in.

In the second part, I worked on fixing the dataset to make it easier for me to work on. I always like to clean up code before I start working on any projects to keep consistency and clear confusion with results. I fixed some spelling mistakes and made sure any literal strings were either the numeric or NaN values they were intended to be.

I picked three different plots to display the data.

The first chart I made presents a bar chart of the top species counts, which poses the questions: Which labels dominate? & Is the dataset heavily imbalanced? This matters because if a few species account for most recordings, then that is important to note for any downstream modeling or sampling strategy.

The second chart I made presents the recordings per country in a bar chart, which poses the questions: Is the dataset geographically skewed? & Are there suspicious categories? I additionally made sure to cap it to the Top 15 to keep the plot readable and interpretable, while still showing the distribution shape.

The third chart I made presents the latitude and longitude scatterplots, which posts the question: Do the coordinates look plausible? I additionally included a filter in the code to remove any garbage coordinate points, which could compress the entire plot and ruin the structure.

If I were to continue with this dataset and project, I would try to make an interactive map using Plotly or Folium. I would also try to care for more of the imbalances in the dataset and validate the consistencies among categories. Lastly, I would want to try to learn how to generate songs from this dataset.