"use client";

import React from "react";

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  className?: string;
  type?: "button" | "submit";
}

export default function Button({
  children,
  onClick,
  disabled = false,
  className = "",
  type = "button",
}: ButtonProps) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`px-5 py-3 rounded-xl font-medium transition-all duration-200
        ${
          disabled
            ? "bg-zinc-700 cursor-not-allowed"
            : "bg-blue-600 hover:bg-blue-700"
        }
        ${className}`}
    >
      {children}
    </button>
  );
}