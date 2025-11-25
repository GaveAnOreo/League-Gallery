import java.util.*;
import java.text.*;
import java.io.*;


public class SupermarketCheckout {


    private static final String CREDENTIALS_FILE = "notepad1.txt";
    private static final String PRODUCTS_FILE = "notepad2.txt";
    private static final String RECEIPT_FILE = "notepad3.txt";
    private static Scanner sc = new Scanner(System.in);
    private static DecimalFormat df = new DecimalFormat("#,##0.00");
    private static Map<String, String[]> productCatalog = new HashMap<>(); // prodcode -> {prodname, unitprice_string}


    public static void main(String[] args) {
        // 0. Load products first, as POS needs it.
        if (!loadProducts()) {
            System.out.println("Error: Could not load products from " + PRODUCTS_FILE + ".");
            System.out.println("Please ensure '" + PRODUCTS_FILE + "' exists in the same directory as the program and is correctly formatted (prodcode,prodname,unitprice).");
            System.out.println("Exiting program.");
            sc.close();
            return;
        }


        // 1. LOGIN
        System.out.println("--- LOGIN ---");
        System.out.print("Enter Username: ");
        String username = sc.nextLine();
        System.out.print("Enter Password: ");
        String password = sc.nextLine();


        if (checkLogin(username, password)) {
            System.out.println("Login successful!");
            runPOS();
        } else {
            System.out.println("Login failed. User not found or incorrect password.");
            // 2. SIGNUP
            System.out.print("Do you want to sign up? (YES/NO): ");
            String signupChoice = sc.nextLine();
            if (signupChoice.equalsIgnoreCase("YES")) {
                handleSignup(); // This method will exit the program
            } else {
                System.out.println("Exiting program. Please run again to try logging in or to sign up.");
            }
        }
        sc.close(); // Close scanner at the very end
    }


    private static boolean checkLogin(String username, String password) {
        File credentialsFile = new File(CREDENTIALS_FILE);
        if (!credentialsFile.exists()) {
            System.out.println("Info: " + CREDENTIALS_FILE + " not found. No users registered yet. Please sign up.");
            return false; // No file, so no users to log in
        }


        try (BufferedReader reader = new BufferedReader(new FileReader(CREDENTIALS_FILE))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(":", 2);
                if (parts.length == 2) {
                    String storedUser = parts[0].trim();
                    String storedPass = parts[1].trim();
                    if (storedUser.equals(username) && storedPass.equals(password)) {
                        return true;
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading credentials file: " + e.getMessage());
        }
        return false;
    }


    private static void handleSignup() {
        System.out.println("--- SIGNUP ---");
        System.out.print("Enter new Username: ");
        String newUsername = sc.nextLine().trim();
        System.out.print("Enter new Password: ");
        String newPassword = sc.nextLine().trim();


        if (newUsername.isEmpty() || newPassword.isEmpty()) {
            System.out.println("Username and Password cannot be empty. Signup failed.");
            System.out.println("Exiting program. Please run again to sign up.");
            System.exit(0); // Stop program
        }
        if (newUsername.contains(":")) {
            System.out.println("Username cannot contain ':'. Signup failed.");
            System.out.println("Exiting program. Please run again to sign up.");
            System.exit(0); // Stop program
        }




        // Check if username already exists
        if (isUsernameTaken(newUsername)) {
            System.out.println("Username '" + newUsername + "' already taken. Please try a different one.");
            System.out.println("Exiting program. Please run again to sign up with a different username.");
            System.exit(0); // Stop program
        }


        try (BufferedWriter writer = new BufferedWriter(new FileWriter(CREDENTIALS_FILE, true))) { // true for append
            writer.write(newUsername + ":" + newPassword);
            writer.newLine();
            System.out.println("Signup successful! Your credentials have been saved to " + CREDENTIALS_FILE);
            System.out.println("Please run the program again to login.");
        } catch (IOException e) {
            System.err.println("Error writing to credentials file: " + e.getMessage());
            System.out.println("Signup failed. Please try again.");
        }
        // Stop the program after signup as per requirement
        System.exit(0);
    }
   
    private static boolean isUsernameTaken(String username) {
        File credentialsFile = new File(CREDENTIALS_FILE);
        if (!credentialsFile.exists()) {
            return false; // No file, so username cannot be taken
        }


        try (BufferedReader reader = new BufferedReader(new FileReader(CREDENTIALS_FILE))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(":", 2);
                if (parts.length > 0 && parts[0].trim().equals(username)) {
                    return true;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading credentials file for username check: " + e.getMessage());
        }
        return false;
    }




    private static boolean loadProducts() {
        File productsFile = new File(PRODUCTS_FILE);
        if (!productsFile.exists()) {
            System.err.println("Error: " + PRODUCTS_FILE + " not found. Cannot load products.");
            return false;
        }


        try (BufferedReader reader = new BufferedReader(new FileReader(PRODUCTS_FILE))) {
            String line;
            int lineNumber = 0;
            while ((line = reader.readLine()) != null) {
                lineNumber++;
                if (line.trim().isEmpty()) continue; // Skip empty lines


                String[] parts = line.split(",", 3); // Split into exactly 3 parts
                if (parts.length == 3) {
                    String prodCode = parts[0].trim();
                    String prodName = parts[1].trim();
                    String unitPriceStr = parts[2].trim();


                    if (prodCode.isEmpty() || prodName.isEmpty() || unitPriceStr.isEmpty()) {
                        System.err.println("Warning: Malformed line in " + PRODUCTS_FILE + " at line " + lineNumber + " (empty field): " + line);
                        continue;
                    }
                    try {
                        Double.parseDouble(unitPriceStr); // Validate price format
                        productCatalog.put(prodCode, new String[]{prodName, unitPriceStr});
                    } catch (NumberFormatException e) {
                        System.err.println("Warning: Invalid price format in " + PRODUCTS_FILE + " at line " + lineNumber + ": \"" + unitPriceStr + "\" for product code " + prodCode);
                    }
                } else {
                    System.err.println("Warning: Malformed line in " + PRODUCTS_FILE + " at line " + lineNumber + " (expected 3 comma-separated values): " + line);
                }
            }
            if (productCatalog.isEmpty()) {
                System.err.println("Error: No valid products loaded from " + PRODUCTS_FILE + ". It might be empty or all lines were incorrectly formatted.");
                return false;
            }
            System.out.println(productCatalog.size() + " products loaded successfully from " + PRODUCTS_FILE);
            return true;
        } catch (IOException e) {
            System.err.println("Error reading products file (" + PRODUCTS_FILE + "): " + e.getMessage());
            return false;
        }
    }
   


    private static void runPOS() {
        System.out.println("\n--- Welcome to ABC Supermarket POS ---");


        String storeName = "ABC Supermarket";
        int quantity = 0;
        double cost = 0.0;
        double subTotalBeforeVat = 0.0;
        int totalQuantity = 0;
        int discountType = 0;
        String discountName = "";
        double discountPercent = 0.0;
        double discountAmount = 0.0;
        double vatAmount = 0.0;
        double lessVat = 0.0;
        double totalBeforeDiscount = 0.0; // This is SubTotalBeforeVat + VatAmount
        double amountDue = 0.0;
        double payment = 0.0;
        double change = 0.0;


        ArrayList<String> productNamesList = new ArrayList<>();
        ArrayList<Double> productPricesList = new ArrayList<>();
        ArrayList<Integer> productQuantitiesList = new ArrayList<>();
        ArrayList<Double> productCostsList = new ArrayList<>();
       
        StringBuilder receiptBuilder = new StringBuilder();


        do {
            System.out.print("Enter Product Code (or type 'DONE' to finish): ");
            String productCode = sc.nextLine().trim();


            if (productCode.equalsIgnoreCase("DONE")) {
                break;
            }


            if (productCatalog.containsKey(productCode)) {
                String[] productDetails = productCatalog.get(productCode);
                String productName = productDetails[0];
                String unitPriceStr = productDetails[1];
                double unitPrice = 0;


                try {
                    unitPrice = Double.parseDouble(unitPriceStr);
                } catch (NumberFormatException e) {
                    System.err.println("Critical Error: Invalid price format for product " + productName + " retrieved from catalog. Skipping.");
                    continue;
                }
               
                System.out.println("Product: " + productName + ", Price: " + df.format(unitPrice));


                System.out.print("Enter Quantity: ");
                String strQuantity = sc.nextLine();
                try {
                    quantity = Integer.parseInt(strQuantity);
                    if (quantity <= 0) {
                        System.out.println("Quantity must be a positive number. Please try again for this product or enter a new product code.");
                        continue;
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid quantity. Please enter a whole number. Please try again for this product or enter a new product code.");
                    continue;
                }
               
                cost = unitPrice * quantity;


                subTotalBeforeVat += cost;
                totalQuantity += quantity;


                productNamesList.add(productName);
                productPricesList.add(unitPrice);
                productQuantitiesList.add(quantity);
                productCostsList.add(cost);


                System.out.println(quantity + " x " + productName + " added. Item cost: " + df.format(cost) + ". Current subtotal: " + df.format(subTotalBeforeVat));


            } else {
                System.out.println("Product code '" + productCode + "' not found. Please try again.");
            }
        } while (true);


        if (totalQuantity == 0) {
            System.out.println("No items were purchased. Exiting POS.");
            return;
        }


        System.out.println("\n--- Discount Selection ---");
        System.out.println("1 - None");
        System.out.println("2 - Senior Citizen (20%)");
        System.out.println("3 - Suki Card (10%)");
        System.out.println("4 - PWD (15%)");
        System.out.print("Enter choice (1-4): ");
        String strDiscountType = sc.nextLine();
        try {
            discountType = Integer.parseInt(strDiscountType);
        } catch (NumberFormatException e) {
            System.out.println("Invalid discount type entered, defaulting to None.");
            discountType = 1;
        }


        switch (discountType) {
            case 1:
                discountPercent = 0.0;
                discountName = "None";
                break;
            case 2:
                discountPercent = 0.20;
                discountName = "Senior Citizen"; // As per image, "SC" might be preferred for brevity on receipt
                break;
            case 3:
                discountPercent = 0.10;
                discountName = "Suki Card";
                break;
            case 4:
                discountPercent = 0.15;
                discountName = "PWD";
                break;
            default:
                System.out.println("Invalid discount choice (" + discountType + "), defaulting to No Discount.");
                discountPercent = 0.0;
                discountName = "None";
        }


        vatAmount = subTotalBeforeVat * 0.12;
        lessVat = subTotalBeforeVat - vatAmount;
        totalBeforeDiscount = subTotalBeforeVat + vatAmount;
       
        discountAmount = totalBeforeDiscount * discountPercent;
        amountDue = totalBeforeDiscount - discountAmount;




        System.out.println("\n--- Payment ---");
        do {
            System.out.println("Amount Due: " + df.format(amountDue));
            System.out.print("Enter Payment: ");
            String strPayment = sc.nextLine();
            try {
                payment = Double.parseDouble(strPayment);
            } catch (NumberFormatException e) {
                System.out.println("Invalid payment amount. Please enter a numeric value.");
                payment = -1;
            }


            if (payment < amountDue) {
                System.out.println("Payment is insufficient. Please enter an amount greater than or equal to the amount due.");
            }


        } while (payment < amountDue);


        change = payment - amountDue;


        Date transactionDate = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");


        // --- Revised Receipt Formatting ---
        receiptBuilder.append("\n\n");
        String centeredStoreName = String.format("%" + ((56 + storeName.length()) / 2) + "s", storeName.toUpperCase());
        receiptBuilder.append(centeredStoreName).append("\n");
        // receiptBuilder.append(String.format("%37s\n", "OFFICIAL RECEIPT")); // Optional: if you want "OFFICIAL RECEIPT"
        receiptBuilder.append("Date: ").append(dateFormat.format(transactionDate)).append("\n");
        receiptBuilder.append("--------------------------------------------------------\n");
        // Column headers matching image more closely (Product ID is not in current item list, using Product Name)
        receiptBuilder.append(String.format("%-20s %11s %10s %10s\n", "Product Name", "Unit Price", "Quantity", "Cost"));
        receiptBuilder.append("--------------------------------------------------------\n");


        for (int i = 0; i < productNamesList.size(); i++) {
            receiptBuilder.append(String.format("%-20.20s %11s %10d %10s\n",
                    productNamesList.get(i),
                    df.format(productPricesList.get(i)),
                    productQuantitiesList.get(i),
                    df.format(productCostsList.get(i))));
        }


        receiptBuilder.append("--------------------------------------------------------\n");
        // Summary section, trying to match image layout
        receiptBuilder.append(String.format("%-25s %8d %18s\n", "Products Bought:", totalQuantity, df.format(subTotalBeforeVat)));
        receiptBuilder.append(String.format("%-25s %27s\n", "12% VAT:", df.format(vatAmount)));
        receiptBuilder.append(String.format("%-25s %27s\n", "Less VAT:", df.format(lessVat)));
       
        String displayDiscountName = discountName;
        if (discountName.equals("Senior Citizen")) displayDiscountName = "SC"; // Abbreviate for receipt if needed


        receiptBuilder.append(String.format("%-25s %-25s\n", "Discount Type:", discountPercent > 0 ? displayDiscountName : "None"));
        if (discountPercent > 0) {
            receiptBuilder.append(String.format("%-25s %27s\n", "Discount Amount:", df.format(discountAmount)));
        }
        receiptBuilder.append(String.format("%-25s %27s\n", "Amount Due:", df.format(amountDue)));
        receiptBuilder.append(String.format("%-25s %27s\n", "Amount Paid:", df.format(payment)));
        receiptBuilder.append(String.format("%-25s %27s\n", "Change:", df.format(change)));
        receiptBuilder.append("========================================================\n");
        String centeredThankYou = String.format("%" + ((56 + "Thank you for shopping!".length()) / 2) + "s", "Thank you for shopping!");
        receiptBuilder.append(centeredThankYou).append("\n");
        receiptBuilder.append("========================================================\n\n");




        System.out.println(receiptBuilder.toString());


        try (BufferedWriter writer = new BufferedWriter(new FileWriter(RECEIPT_FILE, true))) {
            writer.write(receiptBuilder.toString());
            System.out.println("Receipt successfully appended to " + RECEIPT_FILE);
        } catch (IOException e) {
            System.err.println("Error writing receipt to file (" + RECEIPT_FILE + "): " + e.getMessage());
        }
    }
}
