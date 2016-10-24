Feature: I want to be able to play audio

  Scenario:
    Given I press the play button
    When I emit the signal 25
    Then the audio signal starts

  Scenario:
    Given I am not playing audio
    When I give the play section a file called DragonBite.wav
    Then I can play the file

  Scenario:
    Given I am not playing audio
    When I give the play section a file called ""
    Then I can get an error
