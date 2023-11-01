package com.siit.finalproject.entity;

import jakarta.persistence.*;
import lombok.Data;

import java.util.List;


@Data
public class AccountEntity {

    private String username;

    private String password;

}
