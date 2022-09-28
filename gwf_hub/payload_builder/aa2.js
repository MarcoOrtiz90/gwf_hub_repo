var workflow_structure = [
[
{ q_label: "What is the customer&#39;s status? ",
q_id: "status",
 step: "NC/VC",
 type: "string"
},
],
[
],
[
{ q_label: "Was this customer reinstated in the last 90 days? (check cross-org too)",
q_id: "previous_reinstate",
 step: "Reinstates",
 type: "string"
},
{ q_label: "What is the reason of the reinstate?",
q_id: "reinstate_reason",
 step: "Reinstates",
 type: "string"
},
{ q_label: "Is CUI coming back with same payment method?",
q_id: "cui_same_payment",
 step: "Reinstates",
 type: "bool"
},
{ q_label: "If this payment was the reason of enforcement, is that verified?",
q_id: "is_pay_verf",
 step: "Reinstates",
 type: "bool"
},
],
[
]
]