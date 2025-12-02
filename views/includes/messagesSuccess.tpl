% if success and len(success) > 0:
  <div class="successMsg">
    % for msg in success:
      {{ msg }}<br>
    % end
  </div>
% end
