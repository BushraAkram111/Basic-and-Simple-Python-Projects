!npm install generate
import random

def generate_story():
  """Generates a random story."""
  # Get the user's input.
  setting = input("What is the setting of the story? ")
  character = input("Who is the main character? ")
  problem = input("What is the problem the main character faces? ")
  solution = input("How does the main character solve the problem? ")

  # Create a list of phrases for each part of the story.
  settings = ["the desert", "the forest", "the city", "the ocean"]
  characters = ["a knight", "a princess", "a wizard", "a dragon"]
  problems = ["a dragon has kidnapped the princess", "a wizard has cast a spell on the kingdom", "a knight has been accused of a crime", "a princess has lost her crown"]
  solutions = ["the knight slays the dragon", "the wizard breaks the spell", "the knight is exonerated", "the princess finds her crown"]

  # Randomly select a phrase from each list.
  story = "Once upon a time, " + random.choice(settings) + ", " + random.choice(characters) + " faced a problem: " + random.choice(problems) + ". " + random.choice(characters) + " solved the problem by " + random.choice(solutions) + ". The end."

  return story

def main():
  """Generates and prints a random story."""
  story = generate_story()
  print(story)

if __name__ == "__main__":
  main()
