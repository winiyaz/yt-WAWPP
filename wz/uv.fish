#!/bin/fish
echo " "
echo " "
echo " This will install uv python manager "
echo " Main Website - https://docs.astral.sh/uv/"
echo " "
echo " Main Install"
echo " --------------------"
echo " curl -LsSf https://astral.sh/uv/install.sh | sh "
echo ""
echo ""
curl -LsSf https://astral.sh/uv/install.sh | sh
echo ""
echo " Now setting up autocomplete with fish"
echo " echo 'uv generate-shell-completion fish | source' >> ~/.config/fish/config.fish  "
echo " echo 'uvx --generate-shell-completion fish | source' >> ~/.config/fish/config.fish "
echo 'uv generate-shell-completion fish | source' >> ~/.config/fish/config.fish
echo 'uvx --generate-shell-completion fish | source' >> ~/.config/fish/config.fish
echo "Now exit out of shell and try again "
