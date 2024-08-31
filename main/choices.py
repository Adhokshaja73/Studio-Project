USER_STATUS_IN_BOOKING_SESSION = (
                (1, "Joined")
                ,(2, "Left")
                ,(3, "Removed")
)

BOOKING_STATUS_CHOICES = (
        (1, "Booked")
        ,(2, "Cancelled")
)

PAYMENT_STATUS_CHOICES = (
            (1, "Paid")
            ,(2, "Pending")
            ,(3, "Unpaid")
)

USER_TYPE = (
    (1, "Studio Owner")
    ,(2, "User")  # user is defined as anyone who is NOT a studio owner. 
)