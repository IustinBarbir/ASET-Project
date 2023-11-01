package com.siit.finalproject.controller;


import com.siit.finalproject.entity.AccountEntity;
import com.siit.finalproject.service.AccountService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


@RestController
@RequestMapping("/account")
public class AccountController {
    private final AccountService service;

    public AccountController(AccountService service) {
        this.service = service;
    }

    @PostMapping("/add")
    public ResponseEntity<String> addDestination(@Valid @RequestBody AccountEntity account) throws IOException
    {

        service.addAccount(account);
        return new ResponseEntity<>("Account has been added: " , HttpStatus.OK);
    }
}
