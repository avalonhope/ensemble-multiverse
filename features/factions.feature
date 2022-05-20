Feature: factions

  Scenario: check if one faction is a subfaction of another
    Given we have a faction A
      And we have a character C
      And C is a member of faction A
      And we have another faction B
      And faction B is not a subfaction of A
      And faction A is not a subfaction of B
      When C asks to join faction B
      Then C is not allowed to join faction B
 
