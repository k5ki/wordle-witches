"use client";

import { Button } from "@/components/ui/button";
import { deleteCompletedTodos, deleteAllTodos } from "@/actions/todos/actions";

export default function ClearActions() {
  return (
    <div className="flex gap-2 items-center pt-2 border-t">
      <Button
        onClick={async () => {
          await deleteCompletedTodos();
        }}
        size="sm"
        variant="outline"
      >
        Clear Completed Todos
      </Button>
      <Button
        onClick={async () => {
          await deleteAllTodos();
        }}
        className="ml-auto"
        size="sm"
      >
        Clear All Todos
      </Button>
    </div>
  );
}
