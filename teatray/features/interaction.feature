Feature: I want to be able control the audio with interactions
As a BPSP user
I want to touch a tile
So that I can hear the description

  Scenario:
    Given I am silent
    When I emit the signal 25
    Then the audio signal starts
