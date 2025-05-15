# Step 5: Semantic Narrative Authentication Logic
def semantic_authentication_agent(score, prior_auth_score):
    print(f"\nSemantic Authentication Agent Activated")
    print(f"Current Similarity Score: {score}")
    print(f"Prior Authenticated Score: {prior_auth_score}")

    if score >= 0.91:
        print("\nAuthentication Successful")
        return "Authenticate (Pass)", score  
    elif score >= 0.80 and prior_auth_score >= 0.91:
        print("\nAccepted as Continuation of Prior Valid Session")
        return "Authenticate (Pass)", prior_auth_score
    elif 0.75 <= score < 0.91:
        print("\nScore borderline please clarify your input.")
        return "Request Clarification (Retry)", prior_auth_score
    else:
        print("\nAccess Denied — Score too low and no prior valid session.")
        return "Deny Access (Fail)", prior_auth_score
