# pawn color is assigned randomly or
# pawn color can be chosen (choose)

# logic for Player vs Player and Player vs Comp


# BEFORE making a move ALWAYS check if any enemy pawns can be captured - capturing compulsory (can_capture)
# MUST check 2 adjoining fields ALWAYS
# If > 1 in line and vacant fields - must automatically capture all
# check all configurations
# other movements MUST be disabled at this point

# capturing own pawns MUST BE DISABLED

# check if own pawn in from field

# check if to field available/vacant (is_vacant)

# if enemy pawn in the field check if the following field is vacant (is_vacant)
# if YES - compulsory capture - see above
# ALWAYS check if the pawn is own or enemy's (is_enemy)

# if enemy or own pawn reaches promotion line - change to King (K + different colour for each team)
# Kind can move forwards and backwards (check 4 fields)
