"use client";

import { Button } from "@/components/ui/button";
import { signout } from "@/actions/auth/actions";

export default function SignOutButton() {
  return (
    <Button
      variant="ghost"
      onClick={async () => {
        await signout();
      }}
    >
      Sign Out
    </Button>
  );
}
