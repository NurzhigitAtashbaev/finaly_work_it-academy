locations

tour

GET /tour/all/---
tour_all_list


GET
/tour/category/{id}/
---tour_category_read


GET
/tour/comment/
---tour_comment_list


POST
/tour/comment/
---tour_comment_create


PUT
/tour/comment/
---tour_comment_update


POST
/tour/create/
---tour_create_create


DELETE
/tour/delete_comment/{id}/
---tour_delete_comment_delete


GET
/tour/detail/{id}/
---tour_detail_read


POST
/tour/entry/
---tour_entry_create


GET
/tour/types/{id}/
---tour_types_read

Users


PUT
/users/change_password/
---users_change_password_update


PATCH
/users/change_password/
---users_change_password_partial_update


GET
/users/email/verification/{email_verify}
---users_email_verification_read


POST
/users/password_reset/
---An Api View which provides a method to request a password reset token based on an e-mail address
users_password_reset_create


POST
/users/password_reset/confirm/
---users_password_reset_confirm_create


POST
/users/password_reset/validate_token/
---users_password_reset_validate_token_create


GET
/users/profile/{id}
---users_profile_read


PUT
/users/profile/{id}
---users_profile_update


PATCH
/users/profile/{id}
---users_profile_partial_update


DELETE
/users/profile/{id}
---users_profile_delete


GET
/users/profiles/
---users_profiles_list


POST
/users/register/
---users_register_create


POST
/users/token/
---users_token_create


POST
/users/token/refresh/
---users_token_refresh_create


