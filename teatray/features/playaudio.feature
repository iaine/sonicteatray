Feature: I want to be able to play audio

  Scenario:
    Given I press the play button
    When I emit the signal 25
    Then the audio signal starts

  Scenario: One file can play
    Given I am not playing audio
    When I give the play section a file called DragonBite.wav
    Then I can play the file

  Scenario: Two files cannot play at the same time
    Given I am playing "DragonBite.wav"
    When I play "something.wav"
    Then I can get an error

  Scenario: Change file when sensor changes
    Given I am playing "DragonBite.wav"
    When I play "something.wav"
    Then I can get an error
