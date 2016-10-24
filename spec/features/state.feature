Feature: I want to know the state of the player


  Scenario:
    Given I am not playing anything
    When I  set up play
    Then my state is False

  Scenario:
    Given I am not playing anything
    When I ask for "DragonBite.wav"
    Then my state is True

  Scenario:
    Given I am not playing anything
    When I ask for "DragonBite.wav"
    And I ask for "sometest.wav"
    Then my state is True
    And there is a log entry
