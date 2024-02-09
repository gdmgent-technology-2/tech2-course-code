'''
Your task is to simulate the dance between Lox and Faelis. Each creature has its own set of dance moves, and the combination of moves creates various magical effects in the forest. Your goal is to determine the state of the forest after the dance is complete.

The combination of moves from both creatures results in a magical effect:
  Twirl + Twirl = Fireflies light up the forest.
  Leap + Spin = Gentle rain starts falling.
  Spin + Leap = A rainbow appears in the sky.
  Other combinations create different effects that you can dream up.
'''

combinationOfMoves = {
  "TwirlTwirl": "Fireflies light up the forest.",
  "LeapSpin": "Gentle rain starts falling.",
  "SpinLeap": "A rainbow appears in the sky."
}

loxSequences = [ "Twirl", "Leap", "Spin", "Twirl", "Leap" ]
faelisSequences = [ "Spin", "Twirl", "Leap", "Leap", "Spin" ]

# create a function that will take a combination of moves and return the magical effect
def magical_effect(move1, move2):
    if move1 + move2 in combinationOfMoves:
        return combinationOfMoves[move1 + move2]
    else:
        return "No effect."

# loop through the sequences and print the magical effect
def perform_dance():
  effects = []
  for i in range(5):
    effects.append(magical_effect(loxSequences[i], faelisSequences[i]))
  return effects

print(perform_dance())
