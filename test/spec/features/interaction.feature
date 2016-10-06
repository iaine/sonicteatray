Feature: I want to be able control the audio with interactions

  Scenario:
    Given I press the play button
    When I emit the signal 25
    Then the audio signal starts

  Scenario:
    Given I press the play button
    When I emit the signal 26
    Then the audio signal pauses

  Scenario:
    Given I press the play button
    When I emit the signal 27
    Then the audio signal stops
