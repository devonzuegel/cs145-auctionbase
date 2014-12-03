# Implement at least the following:

## Ability to manually change the “current time.”
- [ ] update row in CurrentTime with new time

## Ability for auction users to enter bids on open auctions.

## Automatic auction closing: an auction is “open” after its start time and “closed” when its end time is past or its buy price is reached.

## Ability to browse auctions of interest based on the following input parameters:
- [ ] item ID
- [ ] category
- [ ] item description (This should be a substring search, i.e. not an exact match.)
- [ ] price
- [ ] open/closed status

**Note:** These parameters are compositional (you should be able to browse by category AND price, not category OR price)

## Ability to view all relevant information pertaining to a single auction.
This should be displayed on an individual webpage, and it should display all of the information in your database pertaining to that particular item. In particular, this page should include:
- [ ] the auction’s open/closed status
- [ ] the auction’s bids. You should also display all relevant information for each bid, including
	- the name of the bidder
	- the time of the bid
	- the price of the bid
- [ ] if the auction is closed, it should display the winner of the auction (if a winner exists)

Furthermore, your AuctionBase system must support “realistic” bidding behavior. For example, it should not accept bids that are less than or equal to the current highest bid, bids on closed auctions, or bids from users that don’t exist. Also, as specified above, a bid at the buy price should close the auction. Some of these restrictions may already be checked by your constraints and triggers from Part 2 of the Project; others may require additional triggers or code.

If you do decide to add additional triggers to your database, please create additional `triggerN_add.sql` and `triggerN_drop.sql` files to implement these, and include it as part of your submission. You should also be sure to update your `createDatabase.sh` script to include these extra trigger files. (See the submission instructions at the end of this document for more details.)

# Transactions, errors, and constraint-checking
Commands that modify the database need to be handled carefully, and you should group them into transactions whenever it makes sense for them to be executed as a unit. Using transactional behavior, each unit should either complete in its entirety or, due to failed constraints or other errors, should not modify the database at all. Constraint violations, and other errors due to bad input values or data entry, should be managed gracefully: It must be possible for users to continue interacting with the system after a constraint violation or error is detected, and the database should not be corrupt. You should inform users when errors occur, but your error message need not indicate the exact violation that caused the error.

If it helps, you may assume that AuctionBase has only one user operating on it at a time. Although transactions may be useful for database modifications and constraint-checking, you do not need to worry about transactions as a concurrency-control mechanism. That said, even without special effort your system may turn out to be fairly robust for multiple users.

Task D: Other Miscellaneous Requirements
- [ ] When you generate dynamic HTML pages from your program, please use relative paths, rather than absolute paths, for the links to the various URLs in your website. For example, make your links and forms point to webpage instead of http://www.stanford.edu/~yourusername/cgi-bin/webpage. Relative paths enable us to grade your project in our own webspace.

- You don’t have to implement user authentication. For example, it’s okay to ask the user to enter his/her username
when bidding, without asking for a password.

- [ ] Lastly, a suggestion: it’s a good idea to debug your queries directly in SQLite before hooking them into your web interface. Use the SQLite command-line interface first, to ensure that your queries are working properly and are finishing in a reasonable amount of time. In the command-line interface, you can kill runaway queries using Ctrl-C. Once you are certain your queries are working properly, incorporate them into your web interface.