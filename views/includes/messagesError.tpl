% if errors and len(errors) > 0:
    <div class="errorMsg">
    % for erro in errors.values():
        {{erro}}<br>
    % end
    </div>
% end
