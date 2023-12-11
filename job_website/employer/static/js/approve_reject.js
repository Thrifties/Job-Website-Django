        var dataTable;

        $(document).ready(function () {
            if ($('#applicant_table').length) {
                dataTable = $('#applicant_table').DataTable({
                    
                });

                // Function to handle approval
                $('.approve-button').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    $('#confirmApproval').data('applicant-id', applicantId);
                    $('#approvalModal').modal('show');
                    return false;
                });

                // Function to handle confirm rejection button click
                $('#confirmApproval').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    var approvalReason = $('#approvalReason').val();
                    handleApproval(applicantId, approvalReason);
                    $('#approvalModal').modal('hide');
                    return false; // Prevent default form submission
                });
    
                // Function to handle rejection button click and open modal
                $('.reject-button').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    $('#confirmRejection').data('applicant-id', applicantId);
                    $('#rejectionModal').modal('show');
                    return false;
                });
    
                // Function to handle confirm rejection button click
                $('#confirmRejection').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    var rejectionReason = $('#rejectionReason').val();
                    handleRejection(applicantId, rejectionReason);
                    $('#rejectionModal').modal('hide');
                    return false; // Prevent default form submission
                });
            } else {
                console.error('#applicant_table not found.');
            }
    
            function handleApproval(applicantId, approvalReason) {
                var csrf_token = $("[name=csrfmiddlewaretoken]").val();
            
                if (approvalReason) {
                    $.ajax({
                        type: 'POST',
                        url: 'approve_applicant/' + applicantId + '/',
                        data: {
                            csrfmiddlewaretoken: csrf_token,
                            'approval_reason': approvalReason,
                        },
                        success: function (data) {
                            console.log('Approval success:', data);
                            if (data.status === 'success' && dataTable) {
                                console.log('Reloading DataTable...');
                                location.reload();
                            } else {
                                console.error('Error approving applicant.');
                            }
                        },
                        error: function () {
                            console.error('Error approving applicant. Please try again.');
                        }
                    });
                } else {
                    alert('Approval reason cannot be empty.');
                }
            }
            
            function handleRejection(applicantId, rejectionReason) {
    
                if (rejectionReason) {
                    $.ajax({
                        type: 'POST',
                        url: 'reject_applicant/' + applicantId + '/',
                        data: {
                            csrfmiddlewaretoken: '{% csrf_token %}',
                            'rejection_reason': rejectionReason
                        },
                        success: function (data) {
                            console.log('Rejection success:', data);
                            if (data.status === 'success' && dataTable) {
                                console.log('Reloading DataTable...');
                                location.reload();
                            } else {
                                console.error('Error: Unexpected response');
                                alert('Error: Unexpected response');
                            }
                        },
                        error: function (xhr) {
                            console.error('Error rejecting applicant:', xhr.responseText);
                            alert('Error rejecting applicant. Please try again.');
                        }
                    });
                } else {
                    alert('Rejection reason cannot be empty.');
                }
            }
        });