-- select userID where user won Bid
select bidderID from Bid
where itemID = 1679455238
and amount = (
	select max(amount) from Bid
	where itemID = 1679455238
)