Feature: I want to be able control the audio with interactions
As a BPSP user
I want to touch a tile
So that I can hear the description

  Scenario: I touch a tile attached to the GPIO pin 25
    Given I am silent
    When I emit the signal 25
    Then the audio signal starts

    Given I am silent
    When I emit the signal 25
    Then the audio for "wheatear.mp3" begins

  Scenario: I touch a tile attached to the GPIO pin 26 as 25 is sounding
    Given I am playing audio from 25
    When I emit the signal 26
    Then the audio for "cuckoo.mp3" begins

  Scenario: I touch a tile attached to the GPIO pin 27 with no audio
    Given I am silent
    When I emit the signal 27
    Then I am silent
